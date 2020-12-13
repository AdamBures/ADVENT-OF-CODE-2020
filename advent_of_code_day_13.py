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

print(get_id())
        
