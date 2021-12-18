import os
import math

class Node:
    def __init__(self, value: int = None, left = None, right = None, parent = None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        if self.value is not None:
            return str(self.value)
        else:
            return f'[{self.left.__str__()},{self.right.__str__()}]'

    def __repr__(self):
        return self.__str__()

    def explode(self):
        left_neighbour = self.parent.getLeftNeighbour(self)
        if left_neighbour is not None:
            left_neighbour.value += self.left.value
        right_neighbour = self.parent.getRightNeighbour(self)
        if right_neighbour is not None:
            right_neighbour.value += self.right.value
        self.left, self.right, self.value = None, None, 0

    def split(self):
        self.left = Node(value=self.value // 2, parent=self)
        self.right = Node(value=math.ceil(self.value/2), parent=self)
        self.value = None

    def tryExplode(self):
        if self.value is not None:
            return False
        depth = self.getDepth()
        if depth >= 4 and self.left.value is not None and self.right.value is not None:
            self.explode()
            return True
        if self.left.tryExplode():
            return True
        if self.right.tryExplode():
            return True
        return False

    def trySplit(self):
        if self.value is not None and self.value > 9:
            self.split()
            return True
        if self.left and self.left.trySplit():
            return True
        if self.right and self.right.trySplit():
            return True
        return False

    def getDepth(self, depth = 0):
        if self.parent is None:
            return depth
        else:
            return self.parent.getDepth(depth + 1)

    def getLeftNeighbour(self, prev_node):
        if prev_node == self.left and self.parent is not None:
            return self.parent.getLeftNeighbour(self)
        if prev_node == self.left and self.parent is None:
            return None
        return self.left.getMostRightNode()

    def getRightNeighbour(self, prev_node):
        if prev_node == self.right and self.parent is not None:
            return self.parent.getRightNeighbour(self)
        if prev_node == self.right and self.parent is None:
            return None
        return self.right.getMostLeftNode()

    def getMostRightNode(self):
        if self.right is None:
            return self
        return self.right.getMostRightNode()

    def getMostLeftNode(self):
        if self.left is None:
            return self
        return self.left.getMostLeftNode()

    def printRoot(self):
        node = self
        while node.parent != None:
            node = node.parent
        print(node)

    def magnitude(self):
        if self.value is not None:
            return self.value
        else:
            return 3*self.left.magnitude() + 2*self.right.magnitude()

class BinTree:
    def __init__(self, input):
        self.root = self.buildSubtree(input, None)

    def buildSubtree(self, input, parent):
        node = Node(parent=parent)
        if input[0] == '[':
            sub = input[1:-1]
            split_pos = self.findTopComma(sub)
            node.left, node.right = self.buildSubtree(sub[0:split_pos], node), self.buildSubtree(sub[split_pos+1:], node)
        else:
            node.value = int(input)
        return node

    def findTopComma(self, s):
        if s[0] != '[':
            return s.find(',')
        else:
            i = 1
            l = 1
            r = 0
            while l != r:
                if s[i] == '[':
                    l += 1
                elif s[i] == ']':
                    r += 1
                i += 1
            return i

    def union(self, other):
        self.root = Node(left=self.root, right = other.root)
        self.root.left.parent = self.root
        self.root.right.parent = self.root
        while self.root.tryExplode() or self.root.trySplit():
            pass

    def __str__(self):
        return self.root.__str__()

    def getMagnitude(self):
        return self.root.magnitude()

currentdir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(currentdir, 'input.txt')) as f:
    tree = BinTree(f.readline().strip())
    for row in f:
        tree.union(BinTree(row.strip()))
    print(tree.getMagnitude())
