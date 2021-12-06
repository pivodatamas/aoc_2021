import os
currentdir = os.path.dirname(os.path.abspath(__file__))

count = 0
with open(os.path.join(currentdir, 'input.txt')) as f:
    prev = int(f.readline())
    for line in f:
        next = int(line)
        if prev < next:
            count += 1
        prev = next

print(count)