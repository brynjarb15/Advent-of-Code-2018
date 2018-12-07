import re
import operator
def manhattanDist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

print(manhattanDist(1, 20, 9, 1))

f = open('inputs/day6-input.txt', 'r')


allCords = f.read().split('\n')
#print(allCords)


allCordsTestData = [
    '1, 1',
    '1, 6',
    '8, 3',
    '3, 4',
    '5, 5',
    '8, 9'
]

allCordsTuple = []
for cord in allCords:
    x, y = re.findall('([0-9]+)', cord)
    allCordsTuple.append((int(x), int(y), str(cord)))
#print(allCordsTuple)

#init board
boardSize = 700
board = []
for x in range(boardSize):
    col = []
    for y in range(boardSize):
        col.append('.')
    board.append(col)

# Put the sum to all cords in each place on the board
for x in range(boardSize):
    for y in range(boardSize):
        sumOfDistance = 0
        for cord in allCordsTuple:
            sumOfDistance += manhattanDist(x, y, cord[0], cord[1])
        board[x][y] = sumOfDistance

# Count all the places where the board value is lower than 10000
count = 0
for x in range(boardSize):
    for y in range(boardSize):
        if board[x][y] < 10000:
            count += 1

print(count) # The answer is 38670