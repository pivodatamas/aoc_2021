import os
import re

currentdir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(currentdir, 'input.txt')) as f:
    row = f.readline()
    word = row.strip()
    polys = {}
    row = f.readline()
    row = f.readline()
    while row != '\n' and row != '':
        first, second = row.strip().split(' -> ')
        polys[first] = second
        row = f.readline()

def polymerize(word, polys):
    pos = 0
    while pos < len(word) - 1:
        merged = word[pos] + word[pos+1]
        if polys.get(merged):
            word = word[:pos+1] + polys[merged] + word[pos + 1:]
            pos += 1
        pos += 1
    return word

for i in range(10):
    word = polymerize(word, polys)

chars = { c for c in word }

nums = [word.count(c) for c in chars]
nums.sort()
print(max(nums)-min(nums))
