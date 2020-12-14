import os

os.chdir("Text input")

with open("docking_data.txt") as file:
    data = file.readlines()
    data = [line.strip() for line in data]

def to_binary(dec:int):
    bits = []
    while dec != 0:
        bits.append(str(dec%2))
        dec = dec // 2

    bits.reverse()
    s = ''
    s = s.join(bits)
    
    while len(s) != 36:
        s = '0' + s

    return s

def to_decimal(b):
    while b[0] == '0':
        b = b[1:]

    dec = 0
    for i in range(len(b)):
        j = len(b) - i - 1
        dec += int(b[j]) * (2**i)

    return dec

def get_mem_total():
    mem = {}
    mask = ''

    for line in data:
        line = line.split(' = ')

        if 'mask' in line[0]:
            mask = line[1]

        else:
            loc = line[0][4:-1]

            val = int(line[1])
            valBin = list(to_binary(val))

            # apply the mask
            for i in range(len(mask)):
                if mask[i] != 'X':
                    valBin[i] = mask[i]

            maskedStr = ''
            maskedStr = maskedStr.join(valBin)
            maskedNum = to_decimal(maskedStr)
            mem[loc] = maskedNum

    total = 0
    for i in mem.values():
        total += i
    return total

print(get_mem_total())
