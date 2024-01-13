# RISC-V Assembler and Executor

## 1. String Length

### Registers:
- Set the registers to 0 (!except "cml")

### Memory:
Hello world!\0
```
01001000011001010110110001101100011011110010000001110111011011110111001001101100011001000010000100000000
```
The result will be stored in the "a0" register

## 2. String Copy

### Registers:
- Set the "a0" register to 0 (destination adress)
- Set the "a1" register to 12 (source adress)
- Set the rest of the registers to 0 (!except "cml")

### Memory:
Hello world!\0Buna lume !\0
```
01001000011001010110110001101100011011110010000001110111011011110111001001101100011001000010000100000000010000100111010101101110011000010010000001001100011101010110110101100101001000000010000100000000
```
The result will be stored in RAM

## 3. String Copy (n bytes)

### Registers:
- Set the "a0" register to 0 (destination adress)
- Set the "a1" register to 12 (source adress)
- Set the "a2" register to 4 (n)
- Set the rest of the registers to 0 (!except "cml")

### Memory:
Hello world!\0Buna lume !\0
```
01001000011001010110110001101100011011110010000001110111011011110111001001101100011001000010000100000000010000100111010101101110011000010010000001001100011101010110110101100101001000000010000100000000
```
The result will be stored in RAM