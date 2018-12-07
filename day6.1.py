import re
import operator
def manhattanDist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

print(manhattanDist(1, 20, 9, 1))

f = open('inputs/day6-input.txt', 'r')


allCords = f.read().split('\n')
#print(allCords)

a = {'107, 163': 2322, '103, 274': 1617, '129, 323': 1692, '123, 169': 378, '136, 244': 3145, '130, 176': 2944, '156, 265': 2226, '152, 126': 2218, '176, 98': 2065, '174, 319': 1192, '187, 335': 286, '204, 291': 1159, '191, 323': 502, '218, 271': 2580, '236, 130': 5794, '237, 300': 831, '229, 266': 1126, '230, 270': 352, '253, 257': 2896, '300, 189': 5975, '246, 297': 1346, '279, 84': 1212, '291, 283': 2095, '329, 146': 1961, '314, 118': 1245, '293, 80': 1104, '315, 105': 927, '312, 278': 3705, '347, 114': 3118, '357, 144': 15334}

print(max(a.items(), key=operator.itemgetter(1))[0])


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

# Put icon of each cord if it is the closest to the board
for x in range(boardSize):
    for y in range(boardSize):
        shortestDist = 999999999999999999
        shortestCord = ''
        shortestMoreThanOne = False
        for cord in allCordsTuple:
            dist = manhattanDist(x, y, cord[0], cord[1])
            if dist == shortestDist:
                shortestMoreThanOne = True
            if dist < shortestDist:
                #print(dist)
                shortestMoreThanOne = False
                shortestDist = dist
                shortestCord = cord[2]
        if shortestMoreThanOne:
            board[x][y] = '-'
        else:
            board[x][y] = shortestCord
        

# Count how many each icon is on the board
locations = {}
for x in range(boardSize):
    for y in range(boardSize):
        if board[x][y] in locations:
            locations[board[x][y]] += 1
        else:
            locations[board[x][y]] = 1

print('before removing:', locations)
for x in range(boardSize):
    if board[x][0] in locations:
        locations.pop(board[x][0], None)
    if board[x][boardSize-1] in locations:
        locations.pop(board[x][boardSize-1], None)

for y in range(boardSize):
    if board[0][y] in locations:
        locations.pop(board[0][y], None)
    if board[x][boardSize-1] in locations:
        locations.pop(board[boardSize-1][0], None)


print('after removing:', locations) # The answer is 5975 which comes from grid 300, 189, the remove part is not removing all the cords but by manualy checking which cords area get larger when board is made larger I could remove two cords that where not removed
# shouldBeLikeThisAfterRemoving = {'107, 163': 2322, '103, 274': 1617, '129, 323': 1692, '123, 169': 378, '136, 244': 3145, '130, 176': 2944, '156, 265': 2226, '152, 126': 2218, '176, 98': 2065, '174, 319': 1192, '187, 335': 286, '204, 291': 1159, '191, 323': 502, '218, 271': 2580, '236, 130': 5794, '237, 300': 831, '229, 266': 1126, '230, 270': 352, '253, 257': 2896, '300, 189': 5975, '246, 297': 1346, '279, 84': 1212, '291, 283': 2095, '329, 146': 1961, '314, 118': 1245, '293, 80': 1104, '315, 105': 927, '312, 278': 3705}
# notLikeThis = {'107, 163': 2322, '103, 274': 1617, '129, 323': 1692, '123, 169': 378, '136, 244': 3145, '130, 176': 2944, '156, 265': 2226, '152, 126': 2218, '176, 98': 2065, '174, 319': 1192, '187, 335': 286, '204, 291': 1159, '191, 323': 502, '218, 271': 2580, '236, 130': 5794, '237, 300': 831, '229, 266': 1126, '230, 270': 352, '253, 257': 2896, '300, 189': 5975, '246, 297': 1346, '279, 84': 1212, '291, 283': 2095, '329, 146': 1961, '314, 118': 1245, '293, 80': 1104, '315, 105': 927, '312, 278': 3705, '347, 114': 3118, '357, 144': 15334}

