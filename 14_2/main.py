import os
import json

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

counts = {}
for i in range(len(word) - 1):
    merge = word[i] + word[i + 1]
    if merge not in counts:
        counts[merge] = 1
    else:
        counts[merge] += 1

first, last = word[0], word[-1]

def polymerize(counts, polys):
    prevcount = {key: value for key, value in counts.items()}
    news = {}
    for key, value in prevcount.items():
        if key in polys:
            del counts[key]
            if key[0] + polys[key] in news:
                news[key[0] + polys[key]] += value
            else:
                news[key[0] + polys[key]] = value
            if polys[key] + key[1] in news:
                news[polys[key] + key[1]] += value
            else:
                news[polys[key] + key[1]] = value
    for key, value in news.items():
        if key not in counts:
            counts[key] = value
        else:
            counts[key] += value
    return counts

for i in range(40):
    polymerize(counts, polys)

chars = {}

for key, value in counts.items():
    for c in key:
        if c not in chars:
            chars[c] = 0
        chars[c] += value

chars[first] += 1
chars[last] += 1
nums = [value//2 for value in chars.values()]

print(max(nums) - min(nums))
