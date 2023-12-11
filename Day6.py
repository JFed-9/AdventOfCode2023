with (open('Day6.txt') as file): lines = file.readlines()
time, distance, sum = int(lines[0].split(':')[1].replace(' ','')), int(lines[1].split(':')[1].replace(' ','')), 0
for waiting in range(time): 
    if waiting * (time - waiting) > distance: sum += 1
print("Answer: {0}".format(sum))