import os
os.chdir("Text input")

with open("custom_customs.txt") as file:
    a = file.read().rstrip().split("\n\n")

q = 0
for i in a:
    cur = i.split("\n")
    x = set(list(cur[0]))
    for j in range(len(cur)):
        x &= set(list(cur[j]))
    q += len(x)

for i in range(len(a)):
    a[i] = set(list(a[i]))
    a[i] = set([j for j in a[i] if j != '\n'])

total = 0
cur = a[0]
for i in a:
    total += len(i)
    cur ^= i

print("part 1", total)
print("part 2", q)

