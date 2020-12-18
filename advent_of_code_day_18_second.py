import os
os.chdir("Text input")

class Infix(object):

    def __init__(self, function):
        self.function = function

    def __ror__(self, other):
        return Infix(lambda x, self=self, other=other: self.function(other, x))

    def __or__(self, other):
        return self.function(other)


mul = Infix(lambda x, y: x * y)
add = Infix(lambda x, y: x + y)


def process(line, part=1):
    line = line.replace('*', '|mul|')
    if part == 1:
        line = line.replace('+', '|add|')
    return eval(line)


if __name__ == '__main__':
    assert process('2 * 3 + (4 * 5)') == 26

    count2 = 0
    with open('operation_order.txt') as f:
        for line in f:
            count2 += process(line, part=2)

    print(count2)
