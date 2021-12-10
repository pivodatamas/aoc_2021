import os
import math
from queue import LifoQueue

currentdir = os.path.dirname(os.path.abspath(__file__))

opens = {'(', '[', '{', '<'}
closes = {
    '}': '{',
    ']': '[',
    '>': '<',
    ')': '(', 
}
fails = {
    '}': {'num': 0, 'value': 1197},
    ']': {'num': 0, 'value': 57},
    '>': {'num': 0, 'value': 25137},
    ')': {'num': 0, 'value': 3},
    
    }
with open(os.path.join(currentdir, 'input.txt')) as f:
    for row in f:
        stack = LifoQueue()
        for c in row.strip():
            if c in opens:
                stack.put(c)
            else:
                open = stack.get()
                if open != closes[c]:
                    fails[c]['num'] += 1

    print(sum(v['num']*v['value'] for v in fails.values()))
