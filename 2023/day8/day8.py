from functools import reduce
import math

def count_steps(maps):
    total_steps = 0
    found = False
    current_step = 'AAA'
    while not found:
        for direction in maps['instructions']:
            total_steps += 1
            if maps[current_step][direction] == 'ZZZ':
                found = True
            else:
                current_step = maps[current_step][direction]
    return total_steps

def count_ghost_steps(maps):
    starting_nodes = [node for node in maps.keys() if node[-1] == 'A']
    ending_nodes = [node for node in maps.keys() if node[-1] == 'Z']
    
    cycles = []
    for node in starting_nodes:
        total_steps = 0
        found = False
        current_node = node
        while not found:
            for direction in maps['instructions']:
                total_steps += 1
                found_nodes = []
                if maps[current_node][direction][-1] == 'Z':
                    found = True
                    cycles.append(total_steps)
                    break
                else:
                    current_node = maps[current_node][direction]
    return math.lcm(*cycles)

def process_maps(lines):
    maps = {}
    for i in range(len(lines)):
        if i == 0:
            maps['instructions'] = lines[i]
        else:
            path = lines[i].split(" = ")
            path_start = path[0]
            path_left, path_right = path[1].replace('(','').replace(')', '').split(', ')
            maps[path_start] = {'L': path_left, 'R': path_right}
    return maps

if __name__ == '__main__':
    print("Day 8: Haunted Wasteland")

    for filename in ["day8_example.txt", "day8_input.txt"]:
        print(f"\nProcessing {filename}")

        with open(filename, 'r') as file:
            lines = file.readlines()
            lines = list(map(lambda x: x.strip(), lines))
            lines = list(filter(lambda x: x != '', lines))
        
        maps = process_maps(lines)
        print("Total Steps: " + str(count_steps(maps)))

    for filename in ["day8_ghost_example.txt", "day8_input.txt"]:
        print(f"\nProcessing {filename}")

        with open(filename, 'r') as file:
            lines = file.readlines()
            lines = list(map(lambda x: x.strip(), lines))
            lines = list(filter(lambda x: x != '', lines))
        
        maps = process_maps(lines)
        print("Total Steps: " + str(count_ghost_steps(maps)))