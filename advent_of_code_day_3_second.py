import os
class Main(object):

    os.chdir("Text input")

    def __init__(self):
        self.count = 0
        self.row, self.col = 0,0
        self.lst = []
        self.slopes = [(1,1),(3,1),(5,1), (7,1), (1,2)]
        self.path = "toboggan_trajectory.txt"
        
    def toboggan_trajectory(self, file_map):
        self.total = 1
        for slope in self.slopes:
            while self.row+1 < len(file_map):
                self.row += slope[1]
                self.col += slope[0]
                self.space = file_map[self.row][self.col % len(file_map[self.row])]
                if self.space == "#":
                    self.count += 1
                    
            self.total = self.total * self.count
        print(self.total)
    def read_file(self):
        with open(self.path) as file:
            file_map = file.readlines()
            file_map = [line.strip() for line in file_map]
        Main().toboggan_trajectory(file_map)

if __name__ == "__main__":
    Main().read_file()

with open("toboggan_trajectory.txt") as file:
            file_map = file.readlines()
            file_map = [line.strip() for line in file_map]
slopes = [(1,1),(3,1),(5,1), (7,1), (1,2)]
total = 1
for slope in slopes:
    treeCount = 0
    row, col = 0,0
    while row+1 < len(file_map):
        row += slope[1]
        col += slope[0]
        
        space =  file_map[row][col % len(file_map[row])]
        if space == "#":
            treeCount += 1
    total *= treeCount
print(total)

