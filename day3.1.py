
class Claim:
    x = 0
    y = 0
    width = 0
    height = 0

    def __repr__(self):
        string = "\nx: " + str(self.x) + "\ny: " + str(self.y) +                  "\nwidth: " + str(self.width) +                 "\nHeight: " + str(self.height) + "\n------------\n"
        return string

f = open('inputs/day3-input.txt', 'r')

allClaims = f.read().split('\n')

allClaims2 = [
    '#1 @ 1,3: 4x4',
    '#2 @ 3,1: 4x4',
    '#3 @ 5,5: 2x2'
]

listOfClaims = []

for cl in allClaims:
    cl = cl.split('@ ')[1]
    part1, part2 = cl.split(': ')
    x, y = part1.split(',')
    width, height = part2.split('x')
    newClaim = Claim()
    newClaim.x = int(x)
    newClaim.y = int(y)
    newClaim.width = int(width)
    newClaim.height = int(height)
    listOfClaims.append(newClaim)
    
#print(listOfClaims)

sizeOfBoard = 1500

#Init 1000x1000 board
board = []
for i in range(sizeOfBoard):
    board.append([])

for l in board:
    for i in range(sizeOfBoard):
        l.append(0)


for claim in listOfClaims:
    startX = claim.x
    startY = claim.y
    width = claim.width
    height  = claim.height
    #board[startX][startY] += 1
    for i in range(width):
        for j in range(height):
            board[startX+i][startY+j] += 1
    
count = 0
for x in range(sizeOfBoard):
    for y in range(sizeOfBoard):
        if board[x][y] != 0 and board[x][y] != 1:
            #print('x:', x, 'y;', y)
            count += 1
print('count:', count)

print(board[0][2], board[1][2], board[2][2], board[3][2], board[4][2], board[5][2], board[6][2])
print(board[0][3], board[1][3], board[2][3], board[3][3], board[4][3], board[5][3], board[6][3])
print(board[0][4], board[1][4], board[2][4], board[3][4], board[4][4], board[5][4], board[6][4])
print(board[0][5], board[1][5], board[2][5], board[3][5], board[4][5], board[5][5], board[6][5])
