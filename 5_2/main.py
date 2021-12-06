import os
currentdir = os.path.dirname(os.path.abspath(__file__))

matrix = [[0 for i in range(1000)] for j in range(1000)]

with open(os.path.join(currentdir, 'input.txt')) as f:
    for line in f:
        start, end = line.split('->')
        x1, y1 = start.strip().split(',')
        x2, y2 = end.strip().split(',')
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
        if x1 == x2:
            if y1 > y2:
                for i in range(y2, y1 + 1):
                    matrix[x1][i] += 1
            elif y1 < y2:
                for i in range(y1, y2 + 1):
                    matrix[x1][i] += 1
        elif y1 == y2:
            if x1 > x2:
                for i in range(x2, x1 + 1):
                    matrix[i][y1] += 1
            elif x1 < x2:
                for i in range(x1, x2 + 1):
                    matrix[i][y1] += 1
        elif abs(x1 - x2) == abs(y1 - y2):
            dirX, dirY = 1 if x2 > x1 else -1, 1 if y2 > y1 else -1
            for i in range(abs(x1 - x2) + 1):
                matrix[x1 + i*dirX][y1 + i*dirY] += 1

print(sum(sum(1 if matrix[i][j] > 1 else 0 for j in range(1000)) for i in range(1000)))
