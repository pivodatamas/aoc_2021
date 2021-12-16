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

def process(graph, start_x, start_y):

    Q = {(start_x, start_y)}
    table_size = len(graph)
    dist = [[None for j in range(table_size)] for i in range(table_size)]
    dist[start_x][start_y] = 0

    while Q:
        x, y, min_val = getMinNode(Q, dist)
        Q.remove((x, y))

        #bottom
        if x < table_size - 1:
            replaceIfNeeded(x + 1, y, min_val, Q, dist, graph[x+1][y])
        #right
        if y < table_size - 1:
            replaceIfNeeded(x, y + 1, min_val, Q, dist, graph[x][y+1])
        #top
        if x > 0:
            replaceIfNeeded(x - 1, y, min_val, Q, dist, graph[x-1][y])
        #left
        if y > 0:
            replaceIfNeeded(x, y - 1, min_val, Q, dist, graph[x][y-1])

    return dist

res = process(table, 0, 0)
print(res[-1][-1])
