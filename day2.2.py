f = open('inputs/day2.1-input.txt', 'r')

allStrings = f.read().split('\n')

allStrings2 = [
    'abcde',
    'fghij',
    'klmno',
    'pqrst',
    'fguij',
    'axcye',
    'wvxyz'
]

for string1 in allStrings:
    for string2 in allStrings:
        if string1 == string2:
            continue
        errors = 0
        for letter1, letter2 in zip(string1, string2):
            if letter1 == letter2:
                continue
            if errors == 0:
                errors = 1
                continue
            if errors == 1:
                errors = 2
                break
        if errors == 1 or errors == 0:
            print('s1:', string1)
            print('s2:', string2)
            print('----------')