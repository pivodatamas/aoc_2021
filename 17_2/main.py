import os

currentdir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(currentdir, 'input.txt')) as f:
    inp = f.read().strip()
    split1 = inp.replace('target area: x=', '').replace(' y=', '').split(',')
    xmin, xmax = split1[0].split('..')
    ymin, ymax = split1[1].split('..')
    xmin, xmax, ymin, ymax = int(xmin), int(xmax), int(ymin), int(ymax)

sol_list = []
for x in range(1, xmax + 1):
    for y in range(ymin, 200):
        x_speed = x
        y_speed = y
        x_pos , y_pos = 0, 0
        while y_pos + y_speed >= ymin and x_pos + x_speed <= xmax:
            x_pos += x_speed
            y_pos += y_speed
            if x_speed > 0: x_speed -= 1
            y_speed -= 1

        if y_pos <= ymax and y_pos >= ymin and x_pos <= xmax and x_pos >= xmin:
            sol_list.append((x,y))

print(len(sol_list))
