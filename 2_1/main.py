import os
currentdir = os.path.dirname(os.path.abspath(__file__))

horizontal = 0
depth = 0

with open(os.path.join(currentdir, 'input.txt')) as f:
    for line in f:
        command, step = line.split(' ')
        print(command, step, horizontal, depth)
        if command=='forward':
            horizontal += int(step)
        elif command=='up':
            depth -= int(step)
        elif command=='down':
            depth += int(step)

print(horizontal, depth)

print(horizontal*depth)