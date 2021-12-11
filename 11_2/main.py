import os

currentdir = os.path.dirname(os.path.abspath(__file__))

class Octopus:
    flash_counter = 0
    table = []

    def __init__(self, counter, x, y):
        self.counter = counter
        self.x = x
        self.y = y

    def increase(self):
        self.counter += 1
        if self.counter == 10:
            self.flash()
    
    def flash(self):
        Octopus.flash_counter += 1
        #top
        if self.x > 0:
            Octopus.table[self.x - 1][self.y].increase()
            #topleft
            if self.y > 0:
                Octopus.table[self.x - 1][self.y - 1].increase()
            #topright
            if self.y < len(Octopus.table[self.x]) - 1:
                Octopus.table[self.x - 1][self.y + 1].increase()

        #bottom
        if self.x < len(Octopus.table) - 1:
            Octopus.table[self.x + 1][self.y].increase()
            #bottomleft
            if self.y > 0:
                Octopus.table[self.x + 1][self.y - 1].increase()
            #bottomright
            if self.y < len(Octopus.table[self.x]) - 1:
                Octopus.table[self.x + 1][self.y + 1].increase()

        #leftside
        if self.y > 0:
            Octopus.table[self.x][self.y - 1].increase()

        #rightside
        if self.y < len(Octopus.table[self.x]) - 1:
            Octopus.table[self.x][self.y + 1].increase()

    def resetIfNeeded(self):
        if self.counter > 9:
            self.counter = 0

with open(os.path.join(currentdir, 'input.txt')) as f:
    for x, row in enumerate(f):
        Octopus.table.append([])
        for y, cell in enumerate(row.strip()):
            Octopus.table[x].append(Octopus(int(cell), x, y))

i = 0
found = False

while not found:
    for row in Octopus.table:
        for octopus in row:
            octopus.increase()
    for row in Octopus.table:
        for octopus in row:
            octopus.resetIfNeeded()

    if Octopus.flash_counter == len(Octopus.table) * len(Octopus.table[0]):
        found = True
    
    Octopus.flash_counter = 0
    i += 1

print(i)