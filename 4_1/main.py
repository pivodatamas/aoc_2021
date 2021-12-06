import os
currentdir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(currentdir, 'input.txt')) as f:
    bingos = [int(i) for i in f.readline().split(",")]
    data = f.readlines()


boards = [[] for i in range(len(data)//6)]
for index, row in enumerate(data):
#    print(row, '#')
    if index % 6 == 0: continue
    #if index == 7: break
    listindex = index // 6
    for i in row.split(' '):
        if i.strip() != '':
            boards[listindex].append((int(i.strip()), False))

#print(len(boards[1]))

def checkwin(board) -> bool:
    for i in range(5):
        if all([board[i*5 + j][1] for j in range(5)]):
            return True
        if all([board[j*5 + i][1] for j in range(5)]):
            return True
    return False

def markbingo(board, bingo: int):
    for index in range(len(board)):
        if board[index][0] == bingo:
            board[index] = (board[index][0], True)
last = 0
for index, bing in enumerate(bingos):
    win = -1
    for index, board in enumerate(boards):
        markbingo(board, bing)
        if checkwin(board):
            win = index
            last = bing
            break

    if win != -1: break

def getUnmarkedSum(list) -> int:
    sum = 0
    for i in range(len(list)):
        if not list[i][1]:
            sum += list[i][0]
    return sum

print(win)
print(last*getUnmarkedSum(boards[win]))
