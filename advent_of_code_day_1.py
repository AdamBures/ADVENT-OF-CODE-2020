import os
import itertools
os.chdir("Text input")
lst = []

def report_repair(lst):
    year = 2020
    length = 2
    for numbers in itertools.permutations(lst,length):
        if sum(numbers) == 2020:
            result = numbers[0]*numbers[1]
            print(result)
            break

def read_file():
    file = open("report_repair.txt")
    for number in file:
        lst.append(int(number))
    report_repair(lst)

if __name__ == "__main__":
    report_repair(lst)
    read_file()
