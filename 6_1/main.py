import os
currentdir = os.path.dirname(os.path.abspath(__file__))

class LanternFish:
    def __init__(self, time=8):
        self.time = time


with open(os.path.join(currentdir, 'input.txt')) as f:
    fish_list = [LanternFish(int(time)) for time in f.read().split(',')]

print(len(fish_list))
for i in range(80):
    new_fishes = []
    for fish in fish_list:
        if fish.time == 0:
            fish.time = 7
            new_fishes.append(LanternFish())
        fish.time -= 1
    fish_list += new_fishes

print(len(fish_list))