import os
import fileinput
from collections import defaultdict
class Main(object):

    os.chdir("Text input")

    def __init__(self):
        self.lst = []
        self.path = "password_philosophy.txt"

    def password_philosophy(self):
        self.result = 0
        self.lines = open(self.path)
        for line in self.lines:
            self.words = line.split()
            self.lo,self.hi = [int(x) for x in self.words[0].split("-")]
            self.ch_req = self.words[1][0]
            self.password = self.words[2]
            self.count = defaultdict(int)
            for self.ch in self.password:
                self.count[self.ch] += 1
            if self.lo <= self.count[self.ch_req] <=self.hi:
                self.result += 1
        print(self.result)

Main().password_philosophy()

