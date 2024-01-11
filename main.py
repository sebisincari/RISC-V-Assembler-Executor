import subprocess
import os

subprocess.run("python3 assembler.py", shell=True, check=True)

while True:
    raspuns = input("Doriti sa modificati valorile registrilor?[y/n]: ")
    if (raspuns == "y" or raspuns == "Y"):
        subprocess.run("nano register_file.txt", shell=True, check=True)
        break
    elif (raspuns == "n" or raspuns == "N"):
        break
    else:
        print("Raspuns Invalid.")

ram = input("\nIntroduceti memoria RAM: ")

with open('ram.bin', 'rb') as file:
    binary_data = file.read()

binary_string = ''.join(format(byte, '08b') for byte in binary_data)

binary_string += ram

with open('ram.bin', 'wb') as file:
    file.write(bytes(int(binary_string[i:i+8], 2) for i in range(0, len(binary_string), 8)))

print("\nRAM:")
comanda = "xxd ram.bin"
rezultat = subprocess.run(comanda, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
print(rezultat.stdout)
if rezultat.stderr:
    print("Eroare:", rezultat.stderr)

while True:
    raspuns = input("Doriti sa executati binarul?[y/n]: ")
    if (raspuns == "y" or raspuns == "Y"):
        print("\nRAM:")
        comanda = "xxd ram.bin"
        rezultat = subprocess.run(comanda, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(rezultat.stdout)
        if rezultat.stderr:
            print("Eroare:", rezultat.stderr)
        print("Registrii:")
        subprocess.run("cat register_file.txt", shell=True, check=True)
        break
    elif (raspuns == "n" or raspuns == "N"):
        break
    else:
        print("Raspuns Invalid.")

input("\nApasati ENTER pentru a iesi\n")
os.system('cls' if os.name == 'nt' else 'clear')