import os

currentdir = os.path.dirname(os.path.abspath(__file__))

c = 0

with open(os.path.join(currentdir, 'input.txt')) as f:
    for row in f:
        input, output = row.split('|')
        input, output = input.strip(), output.strip()
        char_dict = [0 for i in range(7)]
        input_list = [[] for i in range(8)]
        for inp in input.split():
            input_list[len(inp)].append(set(inp))
        dict = {i: '' for i in range(10)}
        dict[1] = input_list[2][0]
        dict[8] = input_list[7][0]
        dict[7] = input_list[3][0]
        dict[4] = input_list[4][0]
        char_dict[0] = (dict[7] - dict[1]).pop()
        pairs = (dict[1], dict[4]-dict[1], dict[8]-dict[7]-dict[4])
        for six in input_list[6]:
            if pairs[0].issubset(six) and pairs[1].issubset(six):
                char_dict[6] = (six-pairs[0]-pairs[1]-{char_dict[0]}).pop()
                char_dict[4] = (pairs[2] - {char_dict[6]}).pop()
                dict[9] = six
            if pairs[1].issubset(six) and pairs[2].issubset(six):
                char_dict[5] = (six-pairs[2]-pairs[1]-{char_dict[0]}).pop()
                char_dict[2] = (pairs[0] - {char_dict[5]}).pop()
                dict[6] = six
            if pairs[0].issubset(six) and pairs[2].issubset(six):
                char_dict[1] = (six-pairs[0]-pairs[2]-{char_dict[0]}).pop()
                char_dict[3] = (pairs[1] - {char_dict[1]}).pop()
                dict[0] = six
        
        dict[2] = {char_dict[0], char_dict[2], char_dict[3], char_dict[4], char_dict[6]}
        dict[3] = {char_dict[0], char_dict[2], char_dict[3], char_dict[5], char_dict[6]}
        dict[5] = {char_dict[0], char_dict[1], char_dict[3], char_dict[5], char_dict[6]}
        
        output_list = [{c for c in word} for word in output.split()]
        output_str = ''
        for out in output_list:
            for d, val in dict.items():
                if val == out:
                    output_str += str(d)
                    break
        print(output_str)
        c += int(output_str)
        

print(c)