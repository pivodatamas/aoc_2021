import os
import math

currentdir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(currentdir, 'input.txt')) as f:
    input = [[int(c) for c in row.strip()] for row in f] 

def getAreaSize(i, j, input):
    if i < 0 or i == len(input) or j < 0 or j == len(input[i]) or input[i][j] == 9:
        return 0
    input[i][j] = 9
    return 1 + getAreaSize(i - 1, j, input) + getAreaSize(i + 1, j, input)+ getAreaSize(i, j + 1, input)+ getAreaSize(i, j - 1, input)

low_areas = []

for i, row in enumerate(input):
    for j, cell in enumerate(row):
        if cell != 9:
            low_areas.append(getAreaSize(i, j, input))

low_areas.sort(reverse=True)

print(math.prod(low_areas[:3]))