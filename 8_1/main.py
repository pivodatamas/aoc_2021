import os

currentdir = os.path.dirname(os.path.abspath(__file__))

c = 0

with open(os.path.join(currentdir, 'input.txt')) as f:
    for row in f:
        split1 = row.split('|')[1].strip()
        for num in split1.split():
            if len(num.strip()) in {2,3,4,7}:
                c += 1

print(c)