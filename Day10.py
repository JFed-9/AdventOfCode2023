debug = True
grid = []

start = [-1, -1]

left = [0, -1]
right = [0, 1]
up = [-1, 0]
down = [1, 0]
anyDirection = [-1,-1]

with open('Day10.txt') as file:
    for line in file.readlines():
        grid.append([ch for ch in line.strip()])
        if 'S' in line:
            start = [len(grid) - 1, line.find('S')]

def piece(node):
    return grid[node[0]][node[1]]

path = []

for startingDirection in [up, down, left, right]:
    history = [start]

    history.append([x + y for x, y in zip(history[-1], startingDirection)])

    while (piece(history[-1]) != 'S'):
        current_node = history[-1]
        current_direction = [x - y for x, y in zip(current_node, history[-2])]
        if grid[current_node[0]][current_node[1]] == '7':
            if current_direction == up:
                history.append([x + y for x, y in zip(current_node, left)])
                continue
            if current_direction == right:
                history.append([x + y for x, y in zip(current_node, down)])
                continue
        if grid[current_node[0]][current_node[1]] == 'F':
            if current_direction == up:
                history.append([x + y for x, y in zip(current_node, right)])
                continue
            if current_direction == left:
                history.append([x + y for x, y in zip(current_node, down)])
                continue
        if grid[current_node[0]][current_node[1]] == 'J':
            if current_direction == right:
                history.append([x + y for x, y in zip(current_node, up)])
                continue
            if current_direction == down:
                history.append([x + y for x, y in zip(current_node, left)])
                continue
        if grid[current_node[0]][current_node[1]] == 'L':
            if current_direction == down:
                history.append([x + y for x, y in zip(current_node, right)])
                continue
            if current_direction == left:
                history.append([x + y for x, y in zip(current_node, up)])
                continue
        if grid[current_node[0]][current_node[1]] == '|':
            if current_direction == up or current_direction == down:
                history.append([x + y for x, y in zip(current_node, current_direction)])
                continue
        if grid[current_node[0]][current_node[1]] == '-':
            if current_direction == left or current_direction == right:
                history.append([x + y for x, y in zip(current_node, current_direction)])
                continue
        # You weren't able to go anywhere. Sad.
        break
    if piece(history[-1]) == 'S' and len(history) > 2:
        current_direction = [x - y for x, y in zip(history[-1], history[-2])]
        starting_direction = [x - y for x, y in zip(history[1], history[0])]

        if current_direction == up:
            if starting_direction == right:
                grid[start[0]][start[1]] = 'F'
            if starting_direction == up:
                grid[start[0]][start[1]] = '|'
            if starting_direction == left:
                grid[start[0]][start[1]] = '7'
        if current_direction == down:
            if starting_direction == right:
                grid[start[0]][start[1]] = 'L'
            if starting_direction == down:
                grid[start[0]][start[1]] = '|'
            if starting_direction == left:
                grid[start[0]][start[1]] = 'J'
        if current_direction == left:
            if starting_direction == up:
                grid[start[0]][start[1]] = 'L'
            if starting_direction == down:
                grid[start[0]][start[1]] = 'F'
            if starting_direction == left:
                grid[start[0]][start[1]] = '-'
        if current_direction == right:
            if starting_direction == right:
                grid[start[0]][start[1]] = '-'
            if starting_direction == up:
                grid[start[0]][start[1]] = 'J'
            if starting_direction == down:
                grid[start[0]][start[1]] = '7'
        print(f"Answer for part 1: {len(history)//2}, {history[len(history)//2]}")
        path = history.copy()
        break

included_dots = 0
for row in range(len(grid)):
    if debug: print('\t'.join(grid[row]))
    crosses = 0
    last_angle = ''
    for col in range(len(grid[row])):
        if debug: print(f"{[row,col]}: {piece([row,col])}", end='\t')
        if [row,col] in path:
            if piece([row,col]) == '|':
                crosses += 1
                if debug: print(f"Crosses now equal to {crosses}")
                continue
            if piece([row,col]) in 'LF':
                last_angle = piece([row,col])
                if debug: print(f"Now ignoring things")
                continue
            if piece([row,col]) in '7J':
                if piece([row,col]) == '7' and last_angle == 'L':
                    crosses += 1
                    last_angle = ''
                    if debug: print(f"Crosses now equal to {crosses}")
                    continue
                elif piece([row,col]) == 'J' and last_angle == 'F':
                    crosses += 1
                    last_angle = ''
                    if debug: print(f"Crosses now equal to {crosses}")
                    continue
                else:
                    if debug: print("Done ignoring things. Nothing changed")
                    last_angle = ''
                    continue
            if piece([row,col]) == '-':
                if debug: print("Still ignoring things")
                continue
        if [row,col] not in path and crosses % 2 == 1:
            included_dots += 1
            if debug: print(f"Crosses now equal to {crosses}, so counted 1 more dot")
            continue
        if debug: print(f"Ignoring useless info")
            
    if debug: print(f'\nCurrent dots: {included_dots}\n')

print(f"Answer for part 2: {included_dots}")