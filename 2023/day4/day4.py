from functools import reduce

def calculate_card_points(matches):
    if len(matches) == 0:
        return 0
    points = 0
    for element in matches:
        if points == 0:
            points = 1
        else:
            points *= 2
    return points

scratchcards = {}

with open("day4.txt", 'r') as file:
    lines = file.readlines()

scratchcards_raw = [line.replace("  ", " ").split("|") for line in lines]

for card in scratchcards_raw:
    card_number, winning_numbers = card[0].split(":")
    card_number = int(card_number.replace("Card", "").strip())
    winning_numbers = winning_numbers.strip().split(" ")
    numbers_had = card[1].strip().split(" ")
    scratchcards[card_number] = {
        'winning_numbers': winning_numbers,
        'numbers_had': numbers_had
    }

total_points = 0
total_scratchcards = {}

for card_number in scratchcards.keys():
    total_scratchcards[card_number] = 1

for card_number, numbers in scratchcards.items():
    matches = set(numbers['winning_numbers']).intersection(set(numbers['numbers_had']))
    total_points += int(calculate_card_points(matches))

    if len(matches) > 0:
        for i in range(0, total_scratchcards[card_number]):
            for j in range(1, len(matches)+1):
                total_scratchcards[card_number+j] += 1

print(total_points)
print(reduce((lambda x, y: x + y), total_scratchcards.values()))