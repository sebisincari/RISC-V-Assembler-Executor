from libraries.registers import registers


def creareRegFile(file_path='register_file.txt'):
    global register_file
    global reg_file_init

    with open(file_path, 'r') as file:
        for line in file:
            key, value = line.strip().split()
            register_file[key] = int(value)
            reg_file_init[key] = int(value)
    print(reg_file_init)


def updateRegFile(output_file='register_file.txt'):
    with open(output_file, 'w') as file:
        for key, value in register_file.items():
            file.write(f"{key} {value}\n")


def decode(cod_bin):
    global index
    # print(len(cod_bin))
    # lenght = len(cod_bin)
    while index < register_file['cml'] - 1:
        instructiune = ""
        while instructiune not in functii:
            index += 1
            instructiune += cod_bin[index]
            # print(index)
        print(instructiune)
        # print(index)
        functii[instructiune](cod_bin)

        # apel functie gasita


def readBin():
    with open('ram.txt', 'r') as fisier:
        cod_bin = fisier.readline()
    # print(cod_bin[len()])
    decode(cod_bin)


def decReg(cod_bin):
    global index
    gasit = 0
    binRegCurent = ""
    cheieRegCurent = ""
    while not gasit:
        index += 1
        binRegCurent += cod_bin[index]
        for numeReg, binReg in registers.items():
            if binReg == binRegCurent:
                cheieRegCurent = numeReg
                gasit = 1
                break

    # aici are cheia reg
    return cheieRegCurent


def readRegVal(cheieReg):
    for cheie, val in register_file.items():
        if cheieReg == cheie:
            return val


def writeRegVal(cheieReg, valReg):
    register_file[cheieReg] = valReg


def decIntVal(cod_bin):
    global index
    num = 0
    aux = 1
    # print(index)
    index += 32
    for i in range(32):
        if index < register_file['cml'] - 1:
            if cod_bin[index] == '1':
                num += aux
        aux *= 2
        index -= 1
    # print(index)
    index += 32
    # print("  " + str(num))
    return num


def decIndexJmp(cod_bin):
    global index
    num = 0
    aux = 1
    # print(index)
    index += 16
    for i in range(16):
        if index < register_file['cml'] - 1:
            if cod_bin[index] == '1':
                num += aux
        aux *= 2
        index -= 1
    # print(index)
    index += 16
    # print("  " + str(num))
    return num


def readByte(indexStart, memory):
    strbyte = ""
    # print(indexStart)
    # print(len(cod_bin))
    for i in range(8):
        if indexStart <= len(memory) - 1:
            strbyte += memory[indexStart]
            indexStart += 1
    return strbyte


def intToByte(val):
    byte = ""
    for i in range(8):
        byte = chr(val & 1) + byte
        val = (val >> 1)
    return byte


def addi(cod_bin):
    regD = decReg(cod_bin)
    reg1 = decReg(cod_bin)
    val = decIntVal(cod_bin)
    vReg1 = readRegVal(reg1)
    vRegD = vReg1 + val
    writeRegVal(regD, vRegD)


def j(cod_bin):
    global index
    # print(decIndexJmp(cod_bin))
    index = decIndexJmp(cod_bin) - 1


def li(cod_bin):
    regD = decReg(cod_bin)
    newVal = decIntVal(cod_bin)
    writeRegVal(regD, newVal)


def ret(cod_bin):
    global index
    index = register_file['cml'] + 1


def add(cod_bin):
    regD = decReg(cod_bin)
    reg1 = decReg(cod_bin)
    reg2 = decReg(cod_bin)
    vReg1 = readRegVal(reg1)
    vReg2 = readRegVal(reg2)
    vRegD = vReg1 + vReg2
    writeRegVal(regD, vRegD)


def bge():
    return 0


def beqz(cod_bin):
    global index
    regInterogat = decReg(cod_bin)
    indexSalt = decIndexJmp(cod_bin)
    regVal = readRegVal(regInterogat)
    # print(indexSalt)
    # print(regVal)
    if regVal == 0:
        index = indexSalt - 1


def mv(cod_bin):
    regDest = decReg(cod_bin)
    regSursa = decReg(cod_bin)
    val = readRegVal(regSursa)
    # print(regDest)
    # print(val)
    writeRegVal(regDest, val)


def sd():
    return 0


def fmvs():
    return 0


def lb(cod_bin):
    # global strByte
    regDest = decReg(cod_bin)
    offset = decIntVal(cod_bin)
    regSursa = decReg(cod_bin)
    vRegSursa = readRegVal(regSursa)
    memory = cod_bin[register_file['cml']:]
    # a0-t1*8
    # strByte = ""
    indexByte = (offset + vRegSursa) * 8
    print(indexByte)
    # print(int(vRegSursa))
    # if indexByte < len(cod_bin):
    strByte = readByte(indexByte, memory)
    pow2 = 1
    num = 0
    # print(strByte)
    # strByte = strByte[::-1]
    print(strByte)
    for i in range(7, -1, -1):
        num += pow2 * int(strByte[i])
        pow2 *= 2
    # print(num)
    writeRegVal(regDest, num)


def sb(cod_bin):
    #print("sb")
    # global strByte
    regSursa = decReg(cod_bin)
    offset = decIntVal(cod_bin)
    regDest = decReg(cod_bin)
    valSursa = readRegVal(regSursa)
    valDest = readRegVal(regDest)
    strByte = intToByte(valSursa)
    print (valSursa)
    indexByte = (offset + valDest) * 8
    memory = cod_bin[register_file['cml']:]
    memory_start = memory[:indexByte]
    memory_end = memory[indexByte + 8:]
    memory = memory_start + strByte + memory_end
    cod_bin = cod_bin[:register_file['cml']] + memory
    print (memory)

    #print("sbb")
    with open("ram.txt", 'w') as file:
        for char in cod_bin:
            if char in ['0', '1']:
                file.write(char)
            elif char == '\0':
                file.write('0')


def call():
    return 0


def ld():
    return 0


def lw():
    return 0


def fld():
    return 0


def slli():
    return 0


def fsw():
    return 0


def la():
    return 0


def srai():
    return 0


def ble():
    return 0


def fsubd():
    return 0


def fmuld():
    return 0


def fgts():
    return 0


def flts():
    return 0


def flw():
    return 0


def sub():
    return 0


def bnez():
    return 0


def faddd():
    return 0


def fsqrtd():
    return 0


def bgt():
    return 0


def fmvsx():
    return 0


def fmuls():
    return 0


def fadds():
    return 0


functii = {'111': addi, '1101': j, '1100': li, '1011': ret, '1000': add, '0100': bge, '0000': beqz, '10011': mv,
           '10010': sd, '10101': fmvs, '01011': lb, '01010': sb, '01101': call, '01100': ld, '01111': lw, '00011': fld,
           '101001': slli, '101000': fsw, '011101': la, '011100': srai, '001101': ble, '001100': fsubd, '001111': fmuld,
           '001110': fgts, '001001': flts, '001000': flw, '0001001': sub, '0001000': bnez, '0001011': faddd,
           '0001010': fsqrtd, '0010101': bgt, '0010100': fmvsx, '0010111': fmuls, '0010110': fadds}
register_file = {}
reg_file_init = {}
index = -1
# strByte = ""
creareRegFile()
readBin()
updateRegFile()
