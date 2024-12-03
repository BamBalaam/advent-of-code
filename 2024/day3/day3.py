import re

def get_instructions(corrupted_program, with_conditionals=False):
    cleaner_regex = r'mul\(\d+,\d+\)'
    if with_conditionals:
        cleaner_regex += r'|do\(\)|don\'t\(\)'
    return re.findall(cleaner_regex, corrupted_program)

def manage_conditionals(instructions):
    final_instructions = []
    consume_flag = True
    for instruction in instructions:
        if instruction == ["don't"]:
            consume_flag = False
            continue
        if instruction == ["do"]:
            consume_flag = True
            continue
        if consume_flag:
            final_instructions.append(instruction)
    return final_instructions

def get_program_results(corrupted_program, with_conditionals=False):
    instructions = get_instructions(corrupted_program, with_conditionals)
    instructions = [
        instruction
        .replace('mul', '')
        .replace('(','')
        .replace(')','')
        .split(',')
        for instruction in instructions
    ]
    if with_conditionals:
        instructions = manage_conditionals(instructions)
    results = [
        int(instruction[0]) * int(instruction[1])
        for instruction in instructions
    ]
    return results


if __name__ == '__main__':
    print("Day 3: Mull It Over\n")

    print("Example solutions:\n")
    with open("day3_example_part1.txt", 'r') as file:
        line = file.read()
    print("Part 1: Sum of results: " + str(sum(get_program_results(line))))
    with open("day3_example_part2.txt", 'r') as file:
        line = file.read()
    print("Part 2: Sum of results: " + str(sum(get_program_results(line, with_conditionals=True))))

    print("\nInput solutions:\n")
    with open("day3_input.txt", 'r') as file:
        line = file.read().replace("\n", "")
    print("Part 1: Sum of results: " + str(sum(get_program_results(line))))
    print("Part 2: Sum of results: " + str(sum(get_program_results(line, with_conditionals=True))))
