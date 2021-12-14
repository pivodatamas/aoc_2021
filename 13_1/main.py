import os

currentdir = os.path.dirname(os.path.abspath(__file__))

indices = [[False for j in range(1500)] for i in range(1500)]
folds = []

with open(os.path.join(currentdir, 'input.txt')) as f:
    row = f.readline()
    while row != '\n':
        first, second = row.strip().split(',')
        indices[int(second)][int(first)] = True
        row = f.readline()

    row = f.readline()
    while row != '':
        first, second = row.strip().split('=')
        folds.append((first, int(second)))
        row = f.readline()

def countDots(indices):
    c = 0
    for x in indices:
        for val in x:
            if val:
                c += 1
    return c

for command, value in folds:
    if command == 'fold along x':
        for y in range(len(indices)):
            for x in range(value):
                indices[y][x] = indices[y][x] or indices[y][2*value - x]
                indices[y][2*value - x] = False
        for i, row in enumerate(indices):
            indices[i] = row[:value]

    if command == 'fold along y':
        for y in range(value):
            for x in range(len(indices[0])):
                indices[y][x] = indices[y][x] or indices[2*value - y][x]
        indices = indices[:value][:]
    break

print(countDots(indices))
