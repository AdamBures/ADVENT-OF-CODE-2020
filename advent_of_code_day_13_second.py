import os

os.chdir("Text input")

with open("shuttle_search.txt") as file:
    data = file.readlines()
    data = [line.strip() for line in data]
    data[1] = data[1].split(",")

def get_id():
    arrival = int(data[0])
    ids = data[1]

    lowest = 999999999999
    lowID = 0
    for item in ids:
        if item != "x":
            id = int(item)
        else:
            continue

        idMultiple = arrival // id
        difference = (id * (idMultiple+1)) - arrival
        if difference < lowest:
            lowest = difference
            lowID = id
    return lowID * lowest

def modInverse(a, m): 
    a = a % m 
    for x in range(1, m): 
        if ((a * x) % m == 1): 
            return x 
    return 1

def get_earlies_time():
    ids = []
    fullProduct = 1
    for i in range(len(data[1])):
        item = data[1][i]
        if item != "x":
            k = int(item)
            i = i % k
            ids.append(((k-i)%k,k))
            fullProduct *= k

    total = 0
    for i,k in ids:
        partialProduct = fullProduct // k
        inverse = modInverse(partialProduct, k)
        assert (inverse*partialProduct) % k == 1
        term = inverse*partialProduct*i
        total+=term
    return total%fullProduct

print(get_earlies_time())
