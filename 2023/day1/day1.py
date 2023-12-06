import re

digits_map = {
    'zero': 'z0ero', 'one': 'o1ne', 'two': 't2wo', 'three': 't3hree',
    'four': 'f4our', 'five': 'f5ive', 'six': 's6ix', 'seven': 's7even',
    'eight': 'e8ight', 'nine': 'n9ine'
}

def transform_spelled_digits(line):
    for key, value in digits_map.items():
        if key in line:
            line = line.replace(key, value)
    return line

def get_count_from_list(lines, replace_spelled_digits=False):
    total_count = 0

    for line in lines:
        if replace_spelled_digits:
            line = transform_spelled_digits(line)
        digits = re.findall(r'\d', line)
        if len(digits) == 0:
            pass
        elif len(digits) == 1:
            total_count += int(digits[0] + digits[0])
        else:
            total_count += int(digits[0] + digits[-1])

    return total_count

if __name__ == '__main__':
    print("Day 1: Trebuchet?!\n")

    print("Example solutions:")

    with open("day1_example_part1.txt", 'r') as file:
        lines = file.readlines()

    print("Sum of calibration values: " + str(get_count_from_list(lines)))

    with open("day1_example_part2.txt", 'r') as file:
        lines = file.readlines()

    print("Sum of calibration values with replacements: " + str(get_count_from_list(lines, replace_spelled_digits=True)))

    print("\nInput solutions:")
    with open("day1_input.txt", 'r') as file:
        lines = file.readlines()

    print("Sum of calibration values: " + str(get_count_from_list(lines)))
    print("Sum of calibration values with replacements: " + str(get_count_from_list(lines, replace_spelled_digits=True)))