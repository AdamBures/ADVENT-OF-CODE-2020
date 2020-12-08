import os

os.chdir("Text input")

with open("handheld_halting.txt") as file:
    data = file.readlines()
    data = [line.strip() for line in data]

def get_acc():
    acc = 0
    line = 0
    instructions = []

    
    while line not in instructions:
        instructions.append(line)
        currentInstruction = data[line]
        currentInstruction = currentInstruction.split()
        cmd = currentInstruction[0]
        num = currentInstruction[1]
        if "+" in num:
            num = int(num[1:])
        else:
            num = int(currentInstruction[1])

        if cmd == "acc":
            acc += num
            line += 1
        elif cmd == "jmp":
            line += num

        elif cmd == "nop":
            line += 1

        if line >= len(data):
            return acc, True
        
    return acc, False

acc = get_acc()
print(acc)

for i in range(len(data)):
    if "jmp" in data[i]:
        data[i] = data[i].replace("jmp","nop")
        acc, found = get_acc()
        if found:
            print(acc)
            break
        else:
            data[i] = data[i].replace("nop", "jmp")
