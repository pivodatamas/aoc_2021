import os

def replaceIfNeeded(x, y, val, Q, dist, edge):
    weight = dist[x][y]
    if weight is None or weight > edge + val:
        dist[x][y] = edge + val
        Q.add((x, y))

def getMinNode(Q, dist):
    min_val = None
    min_pos = (0, 0)
    for x, y in Q:
        cur = dist[x][y]
        if cur is not None and (min_val is None or min_val > cur):
            min_pos = (x, y)
            min_val = cur

    return *min_pos, min_val

currentdir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(currentdir, 'input.txt')) as f:
    table = [[int(c) for c in row.strip()] for row in f]

def scaleTable(table: [[int]], scale: int):
    newtable = [[0 for j in range(scale*len(table[0]))] for i in range(scale*len(table))]
    table_size = len(table)
    for i in range(scale):
        for j in range(scale):
            for k in range(table_size):
                for l in range(table_size):
                    new_value = table[k][l]+i+j
                    new_value = 1 + (new_value - 1) % 9
                    newtable[i*table_size + k][j*table_size + l] = new_value
    return newtable

newtable = scaleTable(table, 5)

def process(graph, start_x, start_y):

    Q = {(start_x, start_y)}

    table_size = len(graph)
    dist = [[None for j in range(table_size)] for i in range(table_size)]
    dist[start_x][start_y] = 0

    while Q:
        x, y, min_val = getMinNode(Q, dist)
        Q.remove((x, y))

        if x < table_size - 1:
            replaceIfNeeded(x + 1, y, min_val, Q, dist, graph[x+1][y])
        if y < table_size - 1:
            replaceIfNeeded(x, y + 1, min_val, Q, dist, graph[x][y+1])
        if x > 0:
            replaceIfNeeded(x - 1, y, min_val, Q, dist, graph[x-1][y])
        if y > 0:
            replaceIfNeeded(x, y - 1, min_val, Q, dist, graph[x][y-1])

    return dist

res = process(newtable, 0, 0)
print(res[-1][-1])
