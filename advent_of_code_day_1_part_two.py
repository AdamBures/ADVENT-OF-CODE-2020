import os
import itertools

class Main(object):
    os.chdir("Text input")

    def __init__(self):
        self.year = 2020
        self.length = 3
        self.lst = []
        self.path = "report_repair.txt"
        self.result = 0

    def report_repair(self, lst):
        for self.numbers in itertools.permutations(lst,self.length):
            if sum(self.numbers) == self.year:
                self.result = self.numbers[0] * self.numbers[1] * self.numbers[2]
                print(self.result)
                break
    
    def read_file(self):
        with open(self.path, "r") as file:
            for number in file:
                self.lst.append(int(number))
            Main().report_repair(self.lst)

if __name__ == "__main__":
    Main().read_file()
