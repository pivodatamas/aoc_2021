import os
currentdir = os.path.dirname(os.path.abspath(__file__))

horizontal = 0
aim = 0
depth = 0

with open(os.path.join(currentdir, 'input.txt')) as f:
    for line in f:
        command, step = line.split(' ')
        print(command, step, horizontal, aim)
        if command=='forward':
            horizontal += int(step)
            depth += aim*int(step)
        elif command=='up':
            aim -= int(step)
        elif command=='down':
            aim += int(step)

print(horizontal, depth)

print(horizontal*depth)