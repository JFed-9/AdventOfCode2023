from functools import reduce


def isNum(string):
    return '0' <= string <= '9'

def ProcessInput(lines) -> list[list[str]]:
    grid = []
    newLine = []
    grid.append(['.' for _ in range(len(lines[0])+1)])
    for line in lines:
        newLine = []
        newLine.append('.')
        for ch in line:
            if ch != '\n':
                newLine.append(ch)
        newLine.append('.')
        grid.append(newLine)
    grid.append(['.' for _ in range(len(lines[0])+1)])
    return grid

def GetSums(grid) -> int:
    sum = 0
    num = ''
    start = end = -1
    for i,line in enumerate(grid):
        for j,el in enumerate(line):
            if isNum(el):
                if start == -1:
                    start = j
            else:
                if start != -1:
                    end = j
                    num = int(''.join(grid[i][start:end]))
                    found = False
                    # print("Checking Num: {0}".format(num))
                    for x in range(i - 1, i + 2):
                        for y in range(start - 1, end + 1):
                            # print("\t {0},{1}".format(x,y))
                            if 0 <= x < len(grid) and 0 <= y < len(grid[i]):
                                # print("\t{0}".format(grid[x][y]))
                                if not isNum(grid[x][y]) and grid[x][y] != '.':
                                    found = True
                                    break
                        if found:
                            break
                    if found:
                        print("Valid: {0}".format(num))
                        sum += num
                    else:
                        print("Invalid: {0}".format(num))
                start = -1
    return sum

def GetFullNum(grid, x, y) -> int:
    start = y
    end = y
    while 0 < start and isNum(grid[x][start]):
        start -= 1
    while end < len(grid[x]) and isNum(grid[x][end]):
        end += 1
    num = int(''.join(grid[x][start+1:end]))
    print("Found num: {0}".format(num))
    return num

def GetGearRatios(grid) -> int:
    sum = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '*':
                numbers = []
                for x in range(i - 1, i + 2):
                    for y in range(j - 1, j + 2):
                        if 0 <= x < len(grid) and 0 <= y < len(grid[i]):
                            if isNum(grid[x][y]):
                                numbers.append(GetFullNum(grid,x,y))
                numbers = list(set(numbers))
                if len(numbers) == 2:
                    print("Found gear: {0}".format(numbers))
                    sum += reduce(lambda x, y: x*y, numbers)
    return sum

with (open('Day3.txt') as file):
    lines = file.readlines()

board = ProcessInput(lines)
# sum = GetSums(board)
sum = GetGearRatios(board)
print("Total: {0}".format(sum))