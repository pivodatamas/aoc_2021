import os

currentdir = os.path.dirname(os.path.abspath(__file__))

c = 0


def isLowPoint(i, j, input) -> bool:
    is_lowest = True
    is_lowest = is_lowest and (j == 0 or cell < row[j - 1])
    is_lowest = is_lowest and (j == len(row) - 1 or cell < row[j + 1])
    is_lowest = is_lowest and (i == 0 or cell < input[i - 1][j])
    is_lowest = is_lowest and (i == len(input) - 1 or cell < input[i + 1][j])
    return is_lowest    

with open(os.path.join(currentdir, 'input.txt')) as f:
    input = [[int(c) for c in row.strip()] for row in f]
for i, row in enumerate(input):
    print(row)
    for j, cell in enumerate(row):
        c += cell + 1 if isLowPoint(i, j, input) else 0
print(c)