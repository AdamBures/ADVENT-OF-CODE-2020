import os

os.chdir("Text input")
data = []

with open("binary_boarding.txt") as file:
    for line in file.read().split("\n"):
        data.append(line)

best = 0
for i in range(0,len(data)):
    row = int(data[i][:7].replace("F","0").replace("B", "1"),2)
    column = int(data[i][7:].replace("L","0").replace("R", "1"),2)
    data[i] = (8*row)+column
    best = max(data[i],best)

print(str(best))

missing = (((max(data)+ min(data)) // 2) *(len(data)+1) - sum(data))
print(str(missing))
