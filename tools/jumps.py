from libraries.opcodes import opcodes

jumps = []

with open("./resources/allprograms.txt", "r") as file:
    assembly_code = file.read()

lines = assembly_code.split("\n")
for line in lines:
    if len(line.split("#")[0].strip()) > 0 and line[0] != ".":
        tokens = [i.rstrip(",") for i in line.split("#")[0].strip().split()]
        if ":" in tokens[0]:
            continue
        elif tokens[0] in opcodes:
            for token in tokens[1:]:
                if ((token[-1] == "f") or (token[-1] == "b")) and (tokens[0] != 'call'):
                    if tokens[0] not in jumps:
                        jumps.append(tokens[0])
                        print(tokens[0])
        else:
            print("error")

print(jumps)