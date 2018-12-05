f = open('day1.1-input.txt', 'r')


allNumbers = f.read()
allNumbers = allNumbers.split('\n')
numberSeen = []


string = ''.join(allNumbers)
sum = eval(string)
print(sum)