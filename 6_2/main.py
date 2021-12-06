import os

currentdir = os.path.dirname(os.path.abspath(__file__))

dict = {i: 0 for i in range(9)}

with open(os.path.join(currentdir, 'input.txt')) as f:
    for val in f.read().split(','):
        dict[int(val)] += 1


for i in range(256):
    newdict = {i: 0 for i in range(9)}
    for key, value in dict.items():
        if key == 0:
            newdict[6] += value
            newdict[8] += value
            dict[key] = 0
        else:
            newdict[key - 1] += value
    dict = newdict

print(sum(val for val in dict.values()))