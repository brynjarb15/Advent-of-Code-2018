f = open('inputs/day2.1-input.txt', 'r')

allStrings = f.read().split('\n')

twoCount = 0
threeCount = 0



allStrings2 = [
    'abcdef',
    'bababc',
    'abbcde',
    'abcccd',
    'aabcdd',
    'abcdee',
    'ababab'
]

twoNotSeen = True
threeNotSeen = True

for string in allStrings:
    twoNotSeen = True
    threeNotSeen = True

    for letter in string:
        if string.count(letter) == 2 and twoNotSeen:
            twoCount += 1
            twoNotSeen = False
        if string.count(letter) == 3 and threeNotSeen:
            threeCount += 1
            threeNotSeen = False
        if not (twoNotSeen or threeNotSeen):
            break
    
print('2:', twoCount)
print('3:', threeCount)
print('Checksum: ', twoCount * threeCount)



