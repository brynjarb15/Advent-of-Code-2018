from itertools import cycle

f = open('day1.1-input.txt', 'r')


allNumbers = f.read()
allNumbers = allNumbers.split('\n')
allNumbersCycle = cycle(allNumbers)
numberSeen = {}
currentNumber = 0

for i in allNumbersCycle:
    if not currentNumber in numberSeen:
        numberSeen[currentNumber] = 1
    else:
        break
    currentNumber = eval(str(currentNumber)+ i)
    
    
    

print('this is it', currentNumber)
string = ''.join(allNumbers)
sum = eval(string)
print(sum)