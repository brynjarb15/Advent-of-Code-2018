
class Claim:
    id = 0
    x = 0
    y = 0
    width = 0
    height = 0

    def __repr__(self):
        string = "\nid: " + str(self.id) + "\nx: " + str(self.x) + "\ny: " + str(self.y) + "\nwidth: " + str(
            self.width) + "\nHeight: " + str(self.height) + "\n------------\n"
        return string


f = open('inputs/day3-input.txt', 'r')

allClaims = f.read().split('\n')

allClaims2 = [
    '#1 @ 1,3: 4x4',
    '#2 @ 3,1: 4x4',
    '#3 @ 5,5: 2x2'
]

listOfClaims = []
allIds = []

for cl in allClaims:
    id, cl = cl.split(' @ ')
    allIds.append(id)
    part1, part2 = cl.split(': ')
    x, y = part1.split(',')
    width, height = part2.split('x')
    newClaim = Claim()
    newClaim.id = id
    newClaim.x = int(x)
    newClaim.y = int(y)
    newClaim.width = int(width)
    newClaim.height = int(height)
    listOfClaims.append(newClaim)


for c1 in listOfClaims:
    for c2 in listOfClaims:
        if c1.id == c2.id:
            continue
        left, right = (c1, c2) if c1.x <= c2.x else (c2, c1)
        bottom, top = (c1, c2) if c1.y <= c2.y else (c2, c1)
        if left.x + left.width - 1 >= right.x and bottom.y + bottom.height - 1 >= top.y:
            if left.id in allIds:
                allIds.remove(left.id)
            if right.id in allIds:
                allIds.remove(right.id)

print(allIds)
