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

def game_possible(sets):
    for set_elem in sets:
        for rule_to_check in game_rules.values():
            num_cubes = rule_to_check['regex'].search(set_elem)
            if (
                num_cubes is not None
                and int(num_cubes.group(1)) > rule_to_check['total']
            ):
                return False
    return True

def get_fewest_number_of_cubes_from_sets(sets):
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

def process_games(games):
    possible_game_ids = []
    power_of_sets = []

    for game in games:
        game_id_text, game_sets_text = game.strip().split(":")
        game_id = int(re.compile(r'Game (\d+)').search(game_id_text).group(1))
        sets = game_sets_text.strip().split(";")

        if game_possible(sets):
            possible_game_ids.append(game_id)

        fewest_cubes = get_fewest_number_of_cubes_from_sets(sets)
        power_of_set = reduce((lambda x, y: x * y), fewest_cubes.values())
        power_of_sets.append(power_of_set)

    return possible_game_ids, power_of_sets

if __name__ == '__main__':
    print("Day 2: Cube Conundrum")

    for filename in ["day2_example.txt", "day2_input.txt"]:
        print(f"\nProcessing {filename}")

        with open(filename, 'r') as file:
            lines = file.readlines()

        possible_game_ids, power_of_sets = process_games(lines)

        print("Sum of possible game IDs: " + str(sum(possible_game_ids)))
        print("Sum of power of sets with fewest number of cubes: " + str(sum(power_of_sets)))