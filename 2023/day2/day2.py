from functools import reduce
import re

game_rules = {
    'red': {
        'regex': re.compile(r'(\d+) red'),
        'total': 12
    },
    'green': {
        'regex': re.compile(r'(\d+) green'),
        'total': 13
    },
    'blue': {
        'regex': re.compile(r'(\d+) blue'),
        'total': 14
    }
}

def check_game_possible(sets):
    for set_elem in sets:
        for rule_to_check in game_rules.values():
            num_cubes = rule_to_check['regex'].search(set_elem)
            if (
                num_cubes is not None
                and int(num_cubes.group(1)) > rule_to_check['total']
            ):
                return False
    return True

def get_fewest_number_of_cubes(sets):
    fewest_number_of_cubes = {
        'red': None, 'green': None, 'blue': None
    }
    for set_elem in sets:
        for color, rules in game_rules.items():
            num_cubes = rules['regex'].search(set_elem)
            if num_cubes is not None:
                num_cubes = int(num_cubes.group(1))
                if (
                    fewest_number_of_cubes[color] is None
                    or fewest_number_of_cubes[color] < num_cubes
                ):
                    fewest_number_of_cubes[color] = num_cubes

    return(fewest_number_of_cubes)

with open("day2.txt", 'r') as file:
    lines = file.readlines()

sum_possible_game_ids = 0
sum_power_of_sets = 0

for line in lines:
    game_id_text, game_sets_text = line.strip().split(":")
    
    game_id = int(re.compile(r'Game (\d+)').search(game_id_text).group(1))
    sets = game_sets_text.strip().split(";")

    if check_game_possible(sets):
        sum_possible_game_ids += game_id

    fewest_cubes = get_fewest_number_of_cubes(sets)
    power_of_set = reduce((lambda x, y: x * y), fewest_cubes.values())
    sum_power_of_sets += power_of_set

print(sum_possible_game_ids)
print(sum_power_of_sets)