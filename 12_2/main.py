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

def checkIfSmallTwice(path):
    path_node_list = path.split(',')
    path_node_set = set()
    for node in path_node_list:
        if node in path_node_set and node.islower():
            return True
        path_node_set.add(node)
    return False

paths = []

def DepthSearch(node, path):
    if node.name == 'end':
        paths.append(path.strip(',') + ',end')
    else:
        for nextNode in nodes[node.name].neighbours:
            if nextNode.name != 'start' and (not node.small or node.name not in path or not checkIfSmallTwice(path)):
                DepthSearch(nextNode, path + ',' + node.name)


DepthSearch(nodes['start'], '')

print(len(paths))