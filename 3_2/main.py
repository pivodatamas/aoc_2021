import os
currentdir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(currentdir, 'input.txt')) as f:
    lines = [line.strip() for line in f]

tmp = lines[:]
index = 0
lines_count = len(tmp)

while len(tmp) > 1:
    most_common = '1' if sum([int(i[index]) for i in tmp]) >= len(tmp)/2 else '0'
    tmp = [line for line in tmp if line[index] == most_common]
    index += 1

print(tmp)

index = 0
tmp2 = lines[:]
while len(tmp2) > 1:
    most_common = '1' if sum([int(i[index]) for i in tmp2]) < len(tmp2)/2 else '0'
    tmp2 = [line for line in tmp2 if line[index] == most_common]
    index += 1

print(int(tmp2[0], 2)*int(tmp[0], 2))
