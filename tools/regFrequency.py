registers = ['zero', 'ra', 'sp', 't0', 't1', 't2', 's1', 'a0', 'a1', 'a2', 'a3', 't3', 't4', 't5', 'ft0', 'ft1', 'ft2', 'ft3', 'fa0', 'fa1', 'fa2']
registersFreq = {}

def write_code(assembly_code):
    lines = assembly_code.split("\n")
    for line in lines:
        if len(line.split("#")[0].strip()) > 0 and line[0] != ".":
            tokens = [i.rstrip(",") for i in line.split("#")[0].strip().split()]
            for token in tokens:
                if token in registers:
                    if token in registersFreq:
                        registersFreq[f"{token}"] += 1
                    else:
                        registersFreq[f"{token}"] = 1

with open("./resources/allprograms.txt", "r") as file:
    assembly_code = file.read()
    write_code(assembly_code)

print(registersFreq)
print(len(registersFreq) == len(registers))