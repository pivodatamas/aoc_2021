import os

currentdir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(currentdir, 'input.txt')) as f:
    inp = f.read().strip()
    split1 = inp.replace('target area: x=', '').replace(' y=', '').split(',')
    xmin, xmax = split1[0].split('..')
    ymin, ymax = split1[1].split('..')
    xmin, xmax, ymin, ymax = int(xmin), int(xmax), int(ymin), int(ymax)

sol_list = []

for i in range(200):
    y_speed = i
    y_pos = 0

    while y_pos + y_speed >= ymin:
        y_pos += y_speed
        y_speed -= 1
    if y_pos <= ymax:
        sol_list.append(i)

print(sum(range(max(sol_list) + 1)))
