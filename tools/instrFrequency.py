instr = {}
with open("./resources/allprograms.txt") as f:
    for line in f:
        if line.startswith("."):
            continue
        elif ":" in line:
            continue
        else:
            line = line.split()
            if len(line) == 0:
                continue
            elif line[0] == '#':
                continue
            elif '#' in line:
                tokens = line[:line.index('#')]
            else:
                tokens = line[:]
            opcode = tokens[0]
            if opcode in instr:
                instr[opcode] += 1
            else:
                instr[opcode] = 1

instr = dict(sorted(instr.items(), key=lambda item: item[1], reverse=True))
print(instr)
