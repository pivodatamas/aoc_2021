import os
import math

currentdir = os.path.dirname(os.path.abspath(__file__))

binmap = {  "0": "0000",
            "1": "0001",
            "2": "0010",
            "3": "0011",
            "4": "0100",
            "5": "0101",
            "6": "0110",
            "7": "0111",
            "8": "1000",
            "9": "1001",
            "A": "1010",
            "B": "1011",
            "C": "1100",
            "D": "1101",
            "E": "1110",
            "F": "1111",
}

def convertToBin(s: str) -> str:
    ret = ''
    for c in s:
        ret += binmap[c]
    return ret

with open(os.path.join(currentdir, 'input.txt')) as f:
    binary = convertToBin(f.read().strip())

def operate(values, type):
    if type == 0:
        return sum(values)
    if type == 1:
        return math.prod(values)
    if type == 2:
        return min(values)
    if type == 3:
        return max(values)
    if type == 5:
        return 1 if values[0] > values[1] else 0
    if type == 6:
        return 1 if values[0] < values[1] else 0
    if type == 7:
        return 1 if values[0] == values[1] else 0

def process(binary):
    version, packet_typeId = int(binary[:3], 2), int(binary[3:6], 2)
    if packet_typeId == 4:
        index = 6
        num = ''
        while(True):
            cur = binary[index]
            index += 1
            num += binary[index: index+4]
            index += 4
            if cur == "0":
                break
        return version, index, int(num, 2)
    else:
        length_typeId = int(binary[6])
        if length_typeId == 0:
            total_length = int(binary[7:22], 2)
            sum = 0
            index = 22
            nums = []
            while sum != total_length:
                res = process(binary[index:])
                version += res[0]
                index += res[1]
                sum += res[1]
                nums.append(res[2])
            return version, index, operate(nums, packet_typeId)

        else:
            packet_num = int(binary[7:18], 2)
            index = 18
            nums = []
            for i in range(packet_num):
                res = process(binary[index:])
                version += res[0]
                index += res[1]
                nums.append(res[2])
            return version, index, operate(nums, packet_typeId)

print(process(binary)[2])
