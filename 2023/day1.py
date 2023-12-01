import re

digits_map = {
	'zero': 'z0ero',
	'one': 'o1ne',
	'two': 't2wo',
	'three': 't3hree',
	'four': 'f4our',
	'five': 'f5ive',
	'six': 's6ix',
	'seven': 's7even',
	'eight': 'e8ight',
	'nine': 'n9ine'
}

def get_count_from_list(lines, replace_spelled_digits=False):
	total_count = 0

	for line in lines:
		if replace_spelled_digits:
			for key, value in digits_map.items():
				if key in line:
					line = line.replace(key, value)
		digits = re.findall(r'\d', line)
		if len(digits) == 0:
			pass
		elif len(digits) == 1:
			total_count += int(digits[0] + digits[0])
		else:
			total_count += int(digits[0] + digits[-1])

	return total_count

with open("day1.txt", 'r') as file:
	lines = file.readlines()

print(get_count_from_list(lines))
print(get_count_from_list(lines, replace_spelled_digits=True))