import os

os.chdir("Text input")

with open("adapter_array.txt") as file:
    data = file.readlines()
    data = [int(line.strip()) for line in data]
    data.sort()

data = [0] + data
data.append(max(data)+3)

def adapter_array():
    count1 = 0
    count3 = 0

    for i in range(len(data)-1):
        dif = data[i+1] - data[i]

        if dif == 1:
            count1 += 1

        if dif == 3:
            count3 += 1

    return count1*count3

print(adapter_array())
