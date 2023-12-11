multiplier = 1000000
grid = []
# Read in lines, and widen the rows where needed, indicated by '|' (distance is larger than normal when travelling vertically)
with open('Day11.txt') as file:
    for line in file.readlines():
        line = list(line.strip())
        if not '#' in line:
            line = ['|' for _ in line]
        grid.append(line)
# Widen columns where needed, indicated by '-' (distance is larger than normal when travelling horizontally) or '+' (distance is larger than normal both directions)
for j in range(0, len(grid[0])):
    if not '#' in ''.join([line[j] for line in grid]):
        for i in range(0,len(grid)):
            if grid[i][j] == '|': grid[i][j] = '+'
            if grid[i][j] == '.': grid[i][j] = '-'

galaxies = []
sum = 0

# Find sum of all distances as you find each new galaxy
for row in range(len(grid)):
    for col in [x for x,y in enumerate(grid[row]) if y == '#']:
        for galaxy in galaxies:
            for x in range(min(galaxy[0],row),max(galaxy[0],row)):
                if grid[x][col] in '#.': sum += 1
                if grid[x][col] in '|+': sum += multiplier
            for y in range(min(galaxy[1],col),max(galaxy[1],col)):
                if grid[row][y] in '#.': sum += 1
                if grid[row][y] in '-+': sum += multiplier
        galaxies.append([row,col])

print(f"Answer: {sum}")