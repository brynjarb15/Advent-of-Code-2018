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

def removal(statement,aChar):

   lowercase = aChar.lower()
   uppercase = aChar.upper()

   newstring = statement.replace(lowercase, '').replace(uppercase, '')
   return newstring

f = open('inputs/day5-input.txt', 'r')


string = f.read()
print(len(string))



stringTest = 'dabAcCaCBAcCcaDA'
letters = [
'a',
'b',
'c',
'd',
'e',
'f',
'g',
'h',
'i',
'j',
'k',
'l',
'm',
'n',
'o',
'p',
'q',
'r',
's',
't',
'u',
'v',
'w',
'x',
'y',
'z',
]

smallest = 99999999999999999999
for l in letters:
    nextString = removal(string, l)
    print(l)
    #print(nextString)
    while True:
        returnValue = removePair(nextString)
        if not returnValue:
            break
        else:
            nextString = returnValue
    if len(nextString) < smallest:
        smallest = len(nextString)
    
print(smallest) # answer 4952
