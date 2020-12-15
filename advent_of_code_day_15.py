import os

os.chdir("Text input")

with open("rambunctious_recitation.txt") as file:
    data = file.readlines()
    data = data[0].split(",")
    data = [int(num) for num in data]

def play_memory_game(size):
    memory = {}

    for i in range(0,len(data)-1):
        number = data[i]
        memory[number] = i
    for i in range(len(data)-1, size-1):
        number = data[i]

        if number not in memory:
            data.append(0)
            memory[number] = i
        else:
            j = memory[number]
            newNumber = i-j
            data.append(newNumber)
            memory[number] = i
    return data[-1]

if __name__ == "__main__":
    print(play_memory_game(2020))
    print(play_memory_game(30000000))
