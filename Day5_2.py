import math

def translateMapReverse(num, arr):

    for el in arr:
        if num < (el[0] + el[2]) and num >= el[0]:
            return (num - el[0]) + el[1]

    return num

def checkSeed(seed, seeds):
    for i in range(0, int(len(seeds)/2)):
        # print("Checking Seed ", seed,  " Between: ", seeds[i*2],seeds[i*2] + seeds[(i*2)+1] )
        if seed >= seeds[i*2] and seed < seeds[i*2] + seeds[(i*2)+1]:
            return True
    return False

# Open File
with open("Day5.txt") as file:
    lines = file.read()
    file.close()

ss = []
sf = []
fw = []
wl = []
lt = []
th = []
hl = []


# Split input
sections = lines.split('\n\n')

# Extract seeds
seeds = list(map(int, sections[0].split(': ')[1].split()))

for el in sections[1].split(':\n')[1].split('\n'):
    ss.append(list(map(int,el.split(' '))))
for el in sections[2].split(':\n')[1].split('\n'):
    sf.append(list(map(int,el.split(' '))))
for el in sections[3].split(':\n')[1].split('\n'):
    fw.append(list(map(int,el.split(' '))))
for el in sections[4].split(':\n')[1].split('\n'):
    wl.append(list(map(int,el.split(' '))))
for el in sections[5].split(':\n')[1].split('\n'):
    lt.append(list(map(int,el.split(' '))))
for el in sections[6].split(':\n')[1].split('\n'):
    th.append(list(map(int,el.split(' '))))
for el in sections[7].split(':\n')[1].split('\n'):
    hl.append(list(map(int,el.split(' '))))

# for i in range(0, int(len(seeds) / 2)):
for i in range(0, 10_000_000):
    hum = translateMapReverse(i, hl)
    temp = translateMapReverse(hum, th)
    light = translateMapReverse(temp, lt)
    water = translateMapReverse(light, wl)
    fert = translateMapReverse(water, fw)
    soil = translateMapReverse(fert, sf)
    seed = translateMapReverse(soil, ss)

    # print("SEED: ", i, hum, temp, light, water, fert, soil, seed)

    # print(loc)

    if i % 1_00_000 == 0:
        print("Nothing yet. Checked up to {0}".format(i))

    if checkSeed(seed, seeds):
        print("ANSWER: ", i)
        break