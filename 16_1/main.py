import os

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

def process(binary):
    version, packet_typeId = int(binary[:3], 2), int(binary[3:6], 2)
    if packet_typeId == 4:
        index = 6
        while(True):
            cur = binary[index]
            index += 1
            num = int(binary[index: index+4], 2)
            index += 4
            if cur == "0":
                break
        return version, index
    else:
        length_typeId = int(binary[6])
        if length_typeId == 0:
            total_length = int(binary[7:22], 2)
            sum = 0
            index = 22
            while sum != total_length:
                res = process(binary[index:])
                version += res[0]
                index += res[1]
                sum += res[1]
            return version, index

        else:
            packet_num = int(binary[7:18], 2)
            index = 18
            for i in range(packet_num):
                res = process(binary[index:])
                version += res[0]
                index += res[1]
            return version, index

print(process(binary)[0])
