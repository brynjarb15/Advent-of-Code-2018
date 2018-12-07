
f = open('inputs/day7-input.txt', 'r')


allOrders = f.read().split('\n')
#print(allOrders)



allOrdersTestData = [
    'Step C must be finished before step A can begin.',
    'Step C must be finished before step F can begin.',
    'Step A must be finished before step B can begin.',
    'Step A must be finished before step D can begin.',
    'Step B must be finished before step E can begin.',
    'Step D must be finished before step E can begin.',
    'Step F must be finished before step E can begin.'
]
alphabet = [
'A',
'B',
'C',
'D',
'E',
'F',
'G',
'H',
'I',
'J',
'K',
'L',
'M',
'N',
'O',
'P',
'Q',
'R',
'S',
'T',
'U',
'V',
'W',
'X',
'Y',
'Z'
]

alphabetSmall = [
'A',
'B',
'C',
'D',
'E',
'F'
]

orderDict = {}

# Init dict with all the letters
for letter in alphabet:
    orderDict[letter] = []


for order in allOrders:
    beforeStep = order[5:6]
    step = order.split(' ')[7]
    if not step in orderDict:
        orderDict[step] = [beforeStep]
    else:
        orderDict[step].append(beforeStep)

theFinalOrder = []
print(orderDict)
while True:
    for currentStep in sorted(orderDict):
        if not orderDict[currentStep]:
            theFinalOrder.append(currentStep)
            for step in orderDict:
                if currentStep in orderDict[step]:
                    orderDict[step].remove(currentStep)
            print(theFinalOrder)
            orderDict.pop(currentStep, None)
            break
    if not orderDict:
        break

print(''.join(theFinalOrder)) # Answer BETUFNVADWGPLRJOHMXKZQCISY

