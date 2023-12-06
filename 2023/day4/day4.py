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

def get_scratchcards(lines):
    scratchcards = {}

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

    return scratchcards

def get_points_and_accumulated_scratchcards(scratchcards):
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

    return total_points, total_scratchcards


if __name__ == '__main__':
    print("Day 4: Scratchcards\n")

    for filename in ["day4_example.txt", "day4_input.txt"]:
        print(f"\nProcessing {filename}")

        with open(filename, 'r') as file:
            lines = file.readlines()

        scratchcards = get_scratchcards(lines)
        total_points, total_scratchcards = get_points_and_accumulated_scratchcards(scratchcards)

        print("Total scratchcard points: " + str(total_points))
        print("Accumulated scratchcards: " + str(reduce((lambda x, y: x + y), total_scratchcards.values())))