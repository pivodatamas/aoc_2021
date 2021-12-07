import os

currentdir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(currentdir, 'input.txt')) as f:
    pos_list = [int(val) for val in f.read().split(',')]

onetox_list = [sum(j for j in range(i+1)) for i in range(max(pos_list) + 1)]
print(min(sum(onetox_list[abs(i - pos)] for pos in pos_list) for i in range(max(pos_list) + 1)))
