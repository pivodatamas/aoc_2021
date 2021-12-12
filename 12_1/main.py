import os

currentdir = os.path.dirname(os.path.abspath(__file__))

class Node:

    def __init__(self, name: str) -> None:
        self.neighbours = []
        self.small = name.islower()
        self.name = name

    def addNeighbour(self, node):
        self.neighbours.append(node)

nodes = {}

with open(os.path.join(currentdir, 'input.txt')) as f:
    for row in f:
        first, second = row.strip().split('-')
        if first not in nodes:
            nodes[first] = Node(first)
        if second not in nodes:
            nodes[second] = Node(second)
        nodes[first].addNeighbour(nodes[second])
        nodes[second].addNeighbour(nodes[first])

paths = []

def DepthSearch(node, path):
    if node.name == 'end':
        paths.append(path.strip(',') + ',end')
    else:
        for nextNode in nodes[node.name].neighbours:
            if not nextNode.small or nextNode.name not in path:
                DepthSearch(nextNode, path + ',' + node.name)


DepthSearch(nodes['start'], '')

print(len(paths))