from libraries.opcodes import opcodes
from libraries.registers import registers
from libraries.jumpInstr import jumpInstr

labels = {}

def label_adress(assembly_code):
    section_index = 0
    adress = 0
    lines = assembly_code.split("\n")
    for line in lines:
        if len(line.split("#")[0].strip()) > 0 and line[0] != ".":
            tokens = [i.rstrip(",") for i in line.split("#")[0].strip().split()]
            if ":" in tokens[0]:
                labels[f'section{section_index}'] = {}
                if section_index > 0:
                    for label in labels[f'section{section_index - 1}']:
                        labels[f'section{section_index}'][label] = labels[f'section{section_index - 1}'][label]
                labels[f'section{section_index}'][tokens[0].rstrip(":") + 'b'] = adress
                for i in range(section_index):
                    if tokens[0].rstrip(":") + 'f' not in labels[f'section{i}']:
                        labels[f'section{i}'][tokens[0].rstrip(":") + 'f'] = adress
                section_index += 1
            elif tokens[0] in opcodes:
                adress += len(opcodes[tokens[0]])
                for token in tokens[1:]:
                    if token in registers:
                        adress += len(registers[token])
                    elif ((token[-1] == "f") or (token[-1] == "b")) and (tokens[0] != 'call'):
                        adress += 16
                    elif "(" in token:
                        token = token.rstrip(")").split("(")
                        adress += 32
                        adress += len(registers[token[1]])
                    else:
                        adress += 32
            else:
                print("error")
    for section in labels.values():
        if section:
            first_key = next(iter(section))
            del section[first_key]


def write_code(file, assembly_code):
    section_index = -1
    lines = assembly_code.split("\n")
    for line in lines:
        if len(line.split("#")[0].strip()) > 0 and line[0] != ".":
            tokens = [i.rstrip(",") for i in line.split("#")[0].strip().split()]
            if ":" in tokens[0]:
                section_index += 1
            elif tokens[0] in opcodes:
                file.write(opcodes[tokens[0]])
                for token in tokens[1:]:
                    if token in registers:
                        file.write(registers[token])
                    elif token in labels[f'section{section_index}'] and tokens[0] in jumpInstr:
                        file.write("{:016b}".format(labels[f'section{section_index}'][token]))
                    elif "(" in token:
                        token = token.rstrip(")").split("(")
                        file.write("{:032b}".format((int(token[0]) + (1 << 32)) % (1 << 32)))
                        file.write(registers[token[1]])
                    else:
                        file.write("{:032b}".format((int(token) + (1 << 32)) % (1 << 32)))
            else:
                print("error2")


with open("program.asm", "r") as file:
    assembly_code = file.read()

label_adress(assembly_code)
print(labels)

with open("ram.txt", "w") as file:
    write_code(file, assembly_code)

filebin = open("ram.txt", "r")
fileregin = open("register_file.txt", "r")

binar = filebin.read()
len_binar = len(binar)
regfile = fileregin.read()
regfile = regfile.split()
regfile[-1] = str(len_binar)
sir_formatat = ""
for i in range(0, len(regfile), 2):
    sir_formatat += f"{regfile[i]} {regfile[i + 1]}\n"

filebin.close()
fileregin.close()

# print(sir_formatat)
fileregout = open("register_file.txt", "w")
fileregout.write(sir_formatat)
fileregout.close()
