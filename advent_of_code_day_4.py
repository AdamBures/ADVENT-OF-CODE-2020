import os
import itertools

class Main(object):

    os.chdir("Text input")

    def __init__(self):
        self.lst = []
        self.path = "passport_processing.txt"
        self.count = 1
        self.countValid = 0
        self.currentstring = ""
        self.lst = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]

    def check_passport(self,pp):
        for field in self.lst:
            if field not in pp:
                return False
        return True

    def passport_processing(self):
        file = open(self.path)
        data = file.readlines()
        data = [line.strip() for line in data]
        
        for string in data:
            if string != "":
                self.currentstring += " "+string
            else:
                if Main().check_passport(self.currentstring):
                    self.countValid += 1
                else:
                    self.currentstring = ""
        if Main().check_passport(self.currentstring):
            self.countValid += 1
        print(self.countValid)

if __name__ == "__main__":
    #string = "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm"
    #string2 ="iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl: #cfa07d byr:1929"
    #print(string2.find("hgt"))
    Main().passport_processing()
    #Main().read_file()
