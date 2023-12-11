import json
import math

with open('Day8.txt') as file:
    lines = file.readlines()

left_right = [ch for ch in lines[0].strip()]
desert_map = {}
for line in lines[2:]:
    key, val = line.split(' = ')
    desert_map[key] = {
        'L': val.split(', ')[0][1:],
        'R': val.split(', ')[1][:3],
    }

solutions = {}

my_nodes = [node for node in desert_map.keys() if node.endswith('A')]
lcm = 1

for node in my_nodes:
    curr_inst = 0
    curr_node = node

    while not curr_node.endswith('Z'):
        curr_node = desert_map[curr_node][left_right[curr_inst % len(left_right)]]
        curr_inst += 1
    lcm = lcm*curr_inst//math.gcd(lcm, curr_inst)

print("Answer: ", lcm)