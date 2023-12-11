from functools import reduce

def getFullNumber(line, index):
    num = 0
    temp_index = index
    while temp_index >= 0 and line[temp_index - 1].isdigit():
        temp_index -= 1
    
    while temp_index < len(line) and line[temp_index].isdigit():
        num = (num*10) + int(line[temp_index])
        temp_index += 1
    
    return num

def parseTwoLines(line1, line2):
    row_result = 0
    for idx, el in enumerate(line1):
        if el == '*':
            gear_nums = set()
            for i in range(idx - 1 , idx + 2):
                if idx < 0 or idx >= len(line1):
                    continue
                if (line1[i].isdigit()):
                    gear_nums.add(getFullNumber(line1, i))
                if (line2[i].isdigit()):
                    gear_nums.add(getFullNumber(line2, i))
            print("GEAR" , gear_nums)
            if len(gear_nums) == 2:
                row_result += reduce(lambda x,y: x*y, gear_nums)
    return row_result

def parseThreeLines(line1, line2, line3):
    row_result = 0
    for idx, el in enumerate(line2):
        if el == '*':
            gear_nums = set()
            for i in range(idx - 1 , idx + 2):
                if idx < 0 or idx >= len(line1):
                    continue
                if (line1[i].isdigit()):
                    gear_nums.add(getFullNumber(line1, i))
                if (line2[i].isdigit()):
                    gear_nums.add(getFullNumber(line2, i))
                if (line3[i].isdigit()):
                    gear_nums.add(getFullNumber(line3, i))
            print("GEAR" , gear_nums)
            if len(gear_nums) == 2:
                row_result += reduce(lambda x,y: x*y, gear_nums)
    return row_result
    
with open("Day3.txt") as file:
    lines = file.readlines()

result = 0

line1 = ""
line2 = ""
line3 = ""

for line in lines:
    line = line.strip()

    # Setup
    if line1 == "":
        line1 = line
        continue
    if line2 == "":
        line2 = line
        result += parseTwoLines(line1, line2)
        continue
    if line3 == "":
        line3 = line
        result += parseThreeLines(line1, line2, line3)
        continue
    
    line1 = line2
    line2 = line3
    line3 = line
    
    result += parseThreeLines(line1, line2, line3)    

result += parseTwoLines(line3, line2)

print("Gear Power: {0}".format(result))