import os
currentdir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(currentdir, 'input.txt')) as f:
    bingos = [int(i) for i in f.readline().split(",")]
    data = f.readlines()


boards = [[] for i in range(len(data)//6)]
for index, row in enumerate(data):
    if index % 6 == 0: continue
    listindex = index // 6
    for i in row.split(' '):
        if i.strip() != '':
            boards[listindex].append((int(i.strip()), False))

def checkwin(board) -> bool:
    #printboard(board)
    for i in range(5):
        if all([board[i*5 + j][1] for j in range(5)]):
     #       print(1)
            return True
        if all([board[j*5 + i][1] for j in range(5)]):
      #      print(1)
            return True
    #print(0)
    return False

def markbingo(board, bingo: int):
    for index in range(len(board)):
        if board[index][0] == bingo:
            board[index] = (board[index][0], True)

def printboard(board):
    for i in range(25):
        if i % 5 == 0:
            print('')
        print(board[i], end=' ')
    print('')

last = 0
winners = []

for bing in bingos:
    print('Bing:', bing)
    for board in boards:
        markbingo(board, bing)

    for index, board in enumerate(boards):
        if checkwin(board) and index not in winners:
            print('New winnner', index)
            winners.append(index)

    if len(winners) == 100:
        last = bing
        break

#print(winners)
#printboard(boards[winners[-1]])


def getUnmarkedSum(list) -> int:
    sum = 0
    for i in range(len(list)):
        if not list[i][1]:
            sum += list[i][0]
    return sum

#print(last * getUnmarkedSum(lastwinner))
print(last*getUnmarkedSum(boards[winners[-1]]))
