def removePair(str):
    for first, second in zip(str, str[1:]):
        if first.isupper():
            if second.islower():
                if first.upper() == second.upper():
                    #Found it
                    return str.replace(first+second, '')
        if first.islower():
            if second.isupper():
                if first.upper() == second.upper():
                    #Found it
                    return str.replace(first+second, '')
    return False


f = open('inputs/day5-input.txt', 'r')


string = f.read()
print(len(string))



stringTest = 'dabAcCaCBAcCcaDA'

while True:
    returnValue = removePair(string)
    if not returnValue:
        break
    else:
        string = returnValue
    
print(len(string)) #answer 9462
