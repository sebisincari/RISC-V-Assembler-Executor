ram = input("\nIntroduceti varibalie in memoria RAM: ")

with open('ram.bin', 'rb') as file:
    binary_data = file.read()

binary_string = ''.join(format(byte, '08b') for byte in binary_data)

binary_string += ram

with open('ram.bin', 'wb') as file:
    file.write(bytes(int(binary_string[i:i+8], 2) for i in range(0, len(binary_string), 8)))
