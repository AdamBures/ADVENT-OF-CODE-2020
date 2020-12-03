import os
class Main(object):

    os.chdir("Text input")

    def __init__(self):
        self.lst = []
        self.path = "toboggan_trajectory.txt"
        
    def toboggan_trajectory(self, file_map):
        self.count = 0
        self.row, self.col = 0,0
        while self.row+1 < len(file_map):
            self.row += 1
            self.col += 3
            self.space = file_map[self.row][self.col % len(file_map[self.row])]
            if self.space == "#":
                self.count += 1
        print(self.count)
                

    def read_file(self):
        with open(self.path) as file:
            file_map = file.readlines()
            file_map = [line.strip() for line in file_map]
        print(file_map)
        Main().toboggan_trajectory(file_map)

if __name__ == "__main__":
    Main().read_file()

