# RISC-V Assembler and Executor

## The objective of the project:
The project contains two main scripts: one named "assambler.py", that transforms the RISC-V assembly program to machine code using huffman coding, and the other named "executor.py", that decodes the instructions and executes them. Beside those two there is another script named "memory_modifier.py", that allows to change the binary ram file and adds the variables after the machine code. The "main.py" script is used for providing a user interface(only on linux) that combines those three scripts.

## Project completed by:
```
Andrei Cristian-David(143)
Gheorghe Bogdan-Alexandru(143)
Sincari Sebastian-George(143)
```

## Syntax for running the script:
```
python3 main.py
```

! If the "main.py" script doesn't work, the "assembler.py", "memory-modifier.py" and "executor.py" should be run individually.

### Example RISC-V Assembly Programs
https://marz.utk.edu/my-courses/cosc230/book/example-risc-v-assembly-programs/

The assembly programs are located in the ./code directory (you can add other programs there too).

### Steps:
- Enter the name of the program
- Modify the values of the registers
- Enter the variables in RAM
- Execute the code

<img src="./github/demo.gif" width="100%"/>


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
010010000110010101101100011011000110111100100000010101110110111101110010011001000010000100000000010000100111010101101110011000010010000001001100011101010110110101100101001000000010000100000000
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
010010000110010101101100011011000110111100100000010101110110111101110010011001000010000100000000010000100111010101101110011000010010000001001100011101010110110101100101001000000010000100000000
```
The result will be stored in RAM

## 4. Sum of an Integer Array

### Registers:
- Set the "a0" register to 0 (array adress)
- Set the "a1" register to 6 (array size)
- Set the rest of the registers to 0 (!except "cml")

### Memory:
[6, 5, 4, 2, 3, 1]
```
000000000000000000000000000001100000000000000000000000000000010100000000000000000000000000000100000000000000000000000000000000100000000000000000000000000000001100000000000000000000000000000001
```
The result will be stored in "a0"

## 5. Bubble Sort

### Registers:
- Set the "a0" register to 0 (array adress)
- Set the "a1" register to 6 (array size)
- Set the rest of the registers to 0 (!except "cml")

### Memory:
[6, 5, 4, 2, 3, 1]
```
000000000000000000000000000000000000000000000000000000000000011000000000000000000000000000000000000000000000000000000000000001010000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000000110000000000000000000000000000000000000000000000000000000000000001
```
The result will be stored in RAM

## 6. Binary Search

### Registers:
- Set the "a0" register to 0 (array adress)
- Set the "a1" register to 3 (searched number)
- Set the "a2" register to 6 (array size)
- Set the rest of the registers to 0 (!except "cml")

### Memory:
[1, 2, 3, 4, 5, 6]
```
000000000000000000000000000000010000000000000000000000000000001000000000000000000000000000000011000000000000000000000000000001000000000000000000000000000000010100000000000000000000000000000110
```
The result will be stored in "a0"

 ## 7. Add Element to Singly Linked List

 ### Registers:
- Set the "a0" register to 128 (linked list adress)
- Set the "a1" register to 0 (element adress)
- Set the rest of the registers to 0 (!except "cml")

```
Memory Layout:
+---------------+
|   data (2B)   |  <-- 0
|  +6B padding  |
+---------------+
|   next (8B)   |  <-- 8
|      <16>     |
+---------------+
|   data (2B)   |  <-- 16
|  +6B padding  |  
+---------------+
|   next (8B)   |  <-- 24
|      <32>     |  
+---------------+
|   data (2B)   |  <-- 32
|  +6B padding  |
+---------------+
|   next (8B)   |  <-- 40
|    <NULL>     |
+---------------+
|   ...         |  <-- (continuation of thr memory)
```
### Memory
[(1023, &16), (2047, &32), (511, NULL)]
```
000000000000000000000000000000000000000000000000000000111111111100000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000011111111111000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000001111111110000000000000000000000000000000000000000000000000000000000000000
```
The result will be stored in "a0" and RAM.

## 8. *Reverse a string

### Registers:
- Set the "sp" register to 16 (stack pointer)
- Set the "s1" register to 16 (string adress)
- Set the "ra" register to 16 (return adress)
- Set the rest of the registers to 0 (!except "cml")

### Stack:
```
|               |   <--sp (16)
|  <ret adress> |
|---------------|
|      &s1      |  
|  <str adress> |
+---------------+   <-- 0(start of the memory)
```

```
00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000010000100111010101101110011000010010000001001100011101010110110101100101001000000010000100000000
```
The result should be stored in RAM, but due to the lack of time we didn't make it work (but the 'call' operation and 'strlen' function works).

## How it works:
### ---------------------------------------------Assembler----------------------------------------------

The assembler starts by calculating the adresses of each label in a different section of the program with the "label_adress" function, so that it can jump back and forth to a specific label.

After that, in the "write_code" function, the transformation of the instructions from strings to their binary encoded version takes place. This is done by spliting the text into tokens and transforming them into bits. The bits are then stored in a binary file and they represent the machine code.

### ------------------------------------------Memory-Modifier-----------------------------------------

The memory-modifier script is used to append a certain sequence of bits to the machine code. The sequence represents the memory variables.

### ----------------------------------------------Executor-----------------------------------------------

First step of the execution is storing the ram.bin in a string to be easy to work with. After that the decoding process starts(storing the lenght of the instruction and the operation code) and the call of the instruction itself(every instruction from the RISC-V programs has a function in executor.py with the same name and does the same thing).

Each instruction is decoded from the machine code with the necessary arguments (registers, numbers or offsets) and after that the memory or registers values are modified. At the end of the execution the result is stored in the RAM or in the registers.

!Memory is indexed from 0 and when the adress of an array is put in a register, it should be calculated in Bytes!

An interesting thing in this code is the way we call a function after decoding it and also the management of the registers.