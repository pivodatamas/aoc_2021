import os
currentdir = os.path.dirname(os.path.abspath(__file__))

count_list = [0]*12
count_lines = 0

with open(os.path.join(currentdir, 'input.txt')) as f:
    for line in f:
        count_lines += 1
        for i in range(len(count_list)):
            count_list[i] += int(line[i])

print(count_list)
print(count_lines)

gamma_bin = ''.join(['1' if count > count_lines/2 else '0' for count in count_list])
eps_bin = ''.join(['1' if count <= count_lines/2 else '0' for count in count_list])

print(int(gamma_bin, 2)* int(eps_bin, 2))