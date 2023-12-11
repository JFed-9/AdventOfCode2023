def calcDistance(start, finish):
    dist = abs(finish[0] - start[0]) + abs(finish[1] - start[1])
    return dist

# Open File
with open("Day11.txt") as file:
    lines = [line.strip() for line in file.readlines()]

empty_columns = list(range(0, len(lines[0])))
empty_rows = list(range(0, len(lines)))

for idx, el in enumerate(lines):
    if '#' in el:
        empty_rows.remove(idx)
    for idy, char in enumerate(el):
        if char == '#' and idy in empty_columns:
            empty_columns.remove(idy)

for row in empty_rows:
    lines.insert(row+1, '.'*len(lines[0]))

added_cols = 0

for idx, line in enumerate(lines):
    for val in empty_columns:
        lines[idx] = lines[idx][:(val+added_cols)] + '.' + lines[idx][(val+added_cols):]
        added_cols += 1
    added_cols = 0

galaxies = []
result = 0

for idx, el in enumerate(lines):
    for idy, char in enumerate(el):
        if char == '#':
            for galaxy in galaxies:
                result += calcDistance((idx,idy), galaxy)
            galaxies.append((idx,idy))

print("ANSWER: ", result)