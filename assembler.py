import subprocess
import os
from libraries.opcodes import opcodes
from libraries.registers import registers
from libraries.jumpInstr import jumpInstr

labels = {}
functions = {
    "strlen": "00",
    "printf": "01",
    "scanf": "10",
    "cfunc": "11"
}

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
                adress += 16
                for token in tokens[1:]:
                    if token in registers:
                        adress += 16
                    elif ((token[-1] == "f") or (token[-1] == "b")) and (tokens[0] != 'call'):
                        adress += 16
                    elif "(" in token:
                        token = token.rstrip(")").split("(")
                        adress += 32
                        adress += 16
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
    with open(file, "wb") as bin_file:
        for line in lines:
            if len(line.split("#")[0].strip()) > 0 and line[0] != ".":
                tokens = [i.rstrip(",") for i in line.split("#")[0].strip().split()]
                if ":" in tokens[0]:
                    section_index += 1
                elif tokens[0] in opcodes:
                    towrite = opcodes[tokens[0]]
                    len_towrite = len(towrite)
                    # scriere
                    len_binary = format(len_towrite, '08b')
                    bin_file.write(bytes([int(len_binary[i:i+8], 2) for i in range(0, 8, 8)]))
                    for i in range(0, len(towrite), 8):
                        byte = towrite[i:i+8].ljust(8, '0')
                        bin_file.write(bytes([int(byte, 2)]))
                    # end scriere
                    for token in tokens[1:]:
                        if token in registers:
                            towrite = registers[token]
                            len_towrite = len(towrite)
                            # scriere
                            len_binary = format(len_towrite, '08b')
                            bin_file.write(bytes([int(len_binary[i:i+8], 2) for i in range(0, 8, 8)]))
                            for i in range(0, len(towrite), 8):
                                byte = towrite[i:i+8].ljust(8, '0')
                                bin_file.write(bytes([int(byte, 2)]))
                            # end scriere
                        elif token in labels[f'section{section_index}'] and tokens[0] in jumpInstr:
                            towrite = "{:016b}".format(labels[f'section{section_index}'][token])
                            bin_file.write(int(towrite, 2).to_bytes((len(towrite) + 7) // 8, byteorder='big'))
                        elif "(" in token:
                            token = token.rstrip(")").split("(")
                            towrite = "{:032b}".format((int(token[0]) + (1 << 32)) % (1 << 32))
                            bin_file.write(int(towrite, 2).to_bytes((len(towrite) + 7) // 8, byteorder='big'))
                            towrite = registers[token[1]]
                            len_towrite = len(towrite)
                            # scriere
                            len_binary = format(len_towrite, '08b')
                            bin_file.write(bytes([int(len_binary[i:i+8], 2) for i in range(0, 8, 8)]))
                            for i in range(0, len(towrite), 8):
                                byte = towrite[i:i+8].ljust(8, '0')
                                bin_file.write(bytes([int(byte, 2)]))
                            # end scriere
                        elif token in functions:
                            towrite = functions[token]
                            len_towrite = len(towrite)
                            # scriere
                            len_binary = format(len_towrite, '08b')
                            bin_file.write(bytes([int(len_binary[i:i+8], 2) for i in range(0, 8, 8)]))
                            for i in range(0, len(towrite), 8):
                                byte = towrite[i:i+8].ljust(8, '0')
                                bin_file.write(bytes([int(byte, 2)]))
                            # end scriere
                        else:
                            towrite = "{:032b}".format((int(token) + (1 << 32)) % (1 << 32))
                            bin_file.write(int(towrite, 2).to_bytes((len(towrite) + 7) // 8, byteorder='big'))
                else:
                    print("error2")

os.system('cls' if os.name == 'nt' else 'clear')
while True:
    fisier = input("The name of the program: ")
    try:
        with open(f"./code/{fisier}", "r") as file:
            assembly_code = file.read()
        break
    except FileNotFoundError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("The file doesn't exist. Please enter a valid file.")

label_adress(assembly_code)
write_code("ram.bin", assembly_code)

# afisare binar
print("\nMachine code:")
comanda = "xxd ram.bin"
rezultat = subprocess.run(comanda, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
print(rezultat.stdout)
if rezultat.stderr:
    print("Error:", rezultat.stderr)

# cml
with open('ram.bin', 'rb') as file:
    binary_data = file.read()

binary_string = ''.join(format(byte, '08b') for byte in binary_data)

len_binary = len(binary_string)

with open("register_file.txt", "r") as fileregin:
    regfile = fileregin.read()
    regfile = regfile.split()
    regfile[-1] = str(len_binary)
    sir_formatat = ""
    for i in range(0, len(regfile), 2):
        sir_formatat += f"{regfile[i]} {regfile[i + 1]}\n"

with open("register_file.txt", "w") as fileregout:
    fileregout.write(sir_formatat)
    fileregout.close()
    
