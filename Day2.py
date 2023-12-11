max = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def isPossible(line: str) -> tuple[int, bool]:
    game, colors = line.split(':')
    game = int(game[5:])
    for round in colors.split(';'):
        for group in round.split(', '):
            number, color = group.strip().split(' ')
            if int(number) > max.get(color,0):
                return game, False
    return game, True

def getPower(line: str) -> int:
    cols = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    colors = line.split(':')[1]
    for round in colors.split(';'):
        for group in round.split(', '):
            number, color = group.strip().split(' ')
            if int(number) > cols[color]:
                cols[color] = int(number)
    return cols['red'] * cols['green'] * cols['blue']


with (open('Day2.txt') as file):
    lines = file.readlines()

sum = 0
power = 0
for line in lines:
    game, possible = isPossible(line)
    if possible:
        sum += game
    power += getPower(line)
print("Total: {0}".format(sum))
print("Power: {0}".format(power))