from math import inf
import multiprocessing

def check_num(num):
    global hl, th, lt, wl, fw, sf, ss, seeds
    hum = translateMapReverse(num, hl)
    temp = translateMapReverse(hum, th)
    light = translateMapReverse(temp, lt)
    water = translateMapReverse(light, wl)
    fert = translateMapReverse(water, fw)
    soil = translateMapReverse(fert, sf)
    seed = translateMapReverse(soil, ss)

    if checkSeed(seed,seeds):
        return num
    else:
        return inf

def translateMapReverse(num, arr):
    for el in arr:
        if num < (el[0] + el[2]) and num >= el[0]:
            return (num - el[0]) + el[1]
    return num

def checkSeed(seed, seeds):
    for i in range(0, int(len(seeds)/2)):
        if seed >= seeds[i*2] and seed < seeds[i*2] + seeds[(i*2)+1]:
            return True
    return False

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

sections = lines.split('\n\n')

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

start = 0
end = 100_000_000
step = 1_000_000

if __name__ == "__main__":
    multiprocessing.freeze_support()
    for i in range(start,end,step):
        with multiprocessing.Pool(processes=10) as pool:
            results = pool.map(check_num, range(i, i + step))
        answer = min(results)
        if answer != inf:
            print("Answer: {0}".format(answer))
        else:
            print("Nothing yet. Checked up to {0}".format(i + step))