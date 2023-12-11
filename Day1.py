numbers = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
}

def getNums(line):
    line = line.strip('\n')
    print(line)
    firstInd = lastInd = firstNum = lastNum = -1
    for ind,ch in enumerate(line):
        if (ch >= '0' and ch <= '9'):
            firstInd = ind
            firstNum = int(ch)
            break
    for ind,ch in enumerate(line[::-1]):
        if (ch >= '0' and ch <= '9'):
            lastInd = ind
            lastNum = int(ch)
            break
    print('\tAfter Numbers: ' + str(firstNum) + str(lastNum))
    print('\t\tIndices: ' + str(firstInd) + ' ' + str(lastInd))
    for i in range(0,10):
        index = line.find(numbers.get(i))
        if (0 <= index < firstInd):
            firstInd = index
            firstNum = i
        index = line[::-1].find(numbers.get(i,'!')[::-1])
        if (0 <= index < lastInd):
            lastInd = index
            lastNum = i
    print('\tAfter words: ' + str(firstNum) + str(lastNum))
    print('\t\tIndices: ' + str(firstInd) + ' ' + str(lastInd))
    return str(firstNum) + str(lastNum)

with (open('Day1.txt') as file):
    lines = file.readlines()

sum = 0
for line in lines:
    num = getNums(line)
    sum += int(num)
print("Total: {0}".format(sum))