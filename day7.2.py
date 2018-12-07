
f = open('inputs/day7-input.txt', 'r')


allOrders = f.read().split('\n')
#print(allOrders)




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

allOrdersTestData = [
    'Step C must be finished before step A can begin.',
    'Step C must be finished before step F can begin.',
    'Step A must be finished before step B can begin.',
    'Step A must be finished before step D can begin.',
    'Step B must be finished before step E can begin.',
    'Step D must be finished before step E can begin.',
    'Step F must be finished before step E can begin.'
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

# Init dict with all the letters as keys and empty list as value
for letter in alphabet:
    orderDict[letter] = []

# put the steps into the dictionary
for order in allOrders:
    beforeStep = order[5:6]
    step = order.split(' ')[7]
    if not step in orderDict:
        orderDict[step] = [beforeStep]
    else:
        orderDict[step].append(beforeStep)

workers = []
for i in range(5):
    workers.append(['', -1])

print(workers)


theFinalOrder = []
print(orderDict)



for time in range(99999999):
    for worker in workers:
        if worker[1] == 0: #worker is done and need new job
            currentFinishedWork = worker[0]
            # add the finished work to the final order list
            theFinalOrder.append(currentFinishedWork) 
            worker[0] = ''
            worker[1] = -1
            # Remove the finished work from all the other steps
            for step in orderDict: 
                if currentFinishedWork in orderDict[step]:
                    orderDict[step].remove(currentFinishedWork)
            # Find new work for worker
            for step in sorted(orderDict):
                if not orderDict[step]:
                    # Remove the step from the dict so it can't be choosen again
                    orderDict.pop(step, None)
                    worker[0] = step
                    worker[1] = ord(step) - 4 - 1
                    break
        elif not worker[0]:
            # Find new work for worker
            for step in sorted(orderDict):
                if not orderDict[step]:
                    # Remove the step from the dict so it can't be choosen again
                    orderDict.pop(step, None)
                    worker[0] = step
                    worker[1] = ord(step) - 4 - 1 
                    break
        elif worker[0]:
            worker[1] -= 1
    for d in orderDict:
        if not orderDict[d]:
            print(d)
    print(workers)
    # Check if wokers are done and order dict empty
    if not orderDict:
        for worker in workers:
            if worker[0]:
                break
        else:
            break

print('time:', time)    # Answer is 848, there is some of by 1 error in this so it prints out 849 but the answer is 848
print(''.join(theFinalOrder))