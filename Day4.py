with (open('Day4.txt') as file):
    lines = file.readlines()

total = 0
copies = [1 for _ in lines]
for ind, line in enumerate(lines):
    line = line.split(':')[1].strip()
    winning, mine = line.split('|')
    winning = winning.strip().replace('  ',' ').split(' ')
    mine = mine.strip().replace('  ',' ').split(' ')
    card = 0
    for num in mine:
        if num in winning:
            card += 1
    for i in range(card):
        if ind + i + 1 < len(copies):
            copies[ind + i + 1] += copies[ind]
print(copies)
print("Total: {0}".format(sum(copies)))