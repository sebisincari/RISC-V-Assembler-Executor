import subprocess
import os

subprocess.run("python3 assembler.py", shell=True, check=True)

while True:
    raspuns = input("Do you want to modify the register values?[y/n]: ")
    if (raspuns == "y" or raspuns == "Y"):
        subprocess.run("nano register_file.txt", shell=True, check=True)
        break
    elif (raspuns == "n" or raspuns == "N"):
        break
    else:
        print("Invalid answer.")

subprocess.run("python3 memory_modifier.py", shell=True, check=True)

print("\nRAM:")
comanda = "xxd ram.bin"
rezultat = subprocess.run(comanda, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
print(rezultat.stdout)
if rezultat.stderr:
    print("Error:", rezultat.stderr)

while True:
    raspuns = input("Execute the binary file?[y/n]: ")
    if (raspuns == "y" or raspuns == "Y"):
        subprocess.run("python3 executor.py", shell=True, check=True)
        print("\nRAM:")
        comanda = "xxd ram.bin"
        rezultat = subprocess.run(comanda, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(rezultat.stdout)
        if rezultat.stderr:
            print("Error:", rezultat.stderr)
        print("Registers:")
        subprocess.run("cat register_file.txt", shell=True, check=True)
        break
    elif (raspuns == "n" or raspuns == "N"):
        break
    else:
        print("Invalid answer.")

input("\nPress Enter to exit\n")
os.system('cls' if os.name == 'nt' else 'clear')
