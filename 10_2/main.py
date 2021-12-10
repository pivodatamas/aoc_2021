import os
import math
from queue import LifoQueue

currentdir = os.path.dirname(os.path.abspath(__file__))

opens = {'(': ')',
         '[': ']',
         '{': '}', 
         '<': '>',
}
closes = {
    '}': '{',
    ']': '[',
    '>': '<',
    ')': '(', 
}
fails = {
    '}': {'num': 0, 'value': 3},
    ']': {'num': 0, 'value': 2},
    '>': {'num': 0, 'value': 4},
    ')': {'num': 0, 'value': 1},
    
    }

scores = []

with open(os.path.join(currentdir, 'input.txt')) as f:
    for row in f:
        stack = LifoQueue()
        corrupted = False
        for c in row.strip():
            if c in opens:
                stack.put(c)
            else:
                open = stack.get()
                if open != closes[c]:
                    corrupted = True
                    break
        if not corrupted:
            score = 0
            while not stack.empty():
                b = stack.get()
                score *= 5
                score += fails[opens[b]]['value']
            scores.append(score)

scores.sort()
print(scores[len(scores)//2])
