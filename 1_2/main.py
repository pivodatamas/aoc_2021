import os
currentdir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(currentdir, 'input.txt')) as f:
    data = [int(line) for line in f]

group_size = 3
count = 0

for i in range(len(data)-group_size):
    prev = sum(data[i:i+3])
    print(data[i:i+3], data[i+1:i+group_size+1])
    next = sum(data[i+1:i+group_size+1])
    if prev < next:
        count += 1

print(count)