from functools import reduce

def get_seeds(seeds_raw):
    seeds_raw = seeds_raw.replace('seeds: ', '').strip().split(' ')
    seeds = list(map(int, seeds_raw))
    return seeds

def get_seed_ranges(seeds_raw):
    seeds_raw = seeds_raw.replace('seeds: ', '').strip().split(' ')
    seeds_raw = list(map(int, seeds_raw))
    seed_ranges = [seeds_raw[i:i + 2] for i in range(0, len(seeds_raw), 2)]
    return seed_ranges

def seed_in_ranges(seed, seed_ranges):
    for rng in seed_ranges:
        if rng[0] <= seed <= rng[0] + rng[1]:
            return True
    return False

def get_almanac(pages_raw, reverse=False):
    almanac = {}
    for page in pages_raw:
        if not page[0].isdigit():
            current_type = page.replace(' map:', '')
            current_type = current_type.split('-')[-1]
            almanac[current_type] = []
        else:
            ranges = page.split(' ')
            ranges = list(map(int, ranges))

            if not reverse:
                almanac[current_type].append({
                    'destination': (ranges[0], ranges[0]+ranges[2]-1),
                    'start': (ranges[1], ranges[1]+ranges[2]-1),
                })
            else:
                almanac[current_type].append({
                    'start': (ranges[0], ranges[0]+ranges[2]-1),
                    'destination': (ranges[1], ranges[1]+ranges[2]-1),
                })
    return almanac

def get_destination_from_start_position(start_position, almanac, paths):
    numbers = [start_position]
    numbers.extend([None for i in range(7)])

    for i in range(0, len(numbers)-1):
        ranges = almanac[paths[i]]
        for rng in ranges:
            if rng['start'][0] <= numbers[i] <= rng['start'][1]:
                diff = (numbers[i] - rng['start'][0])
                offset = rng['destination'][0] + diff
                numbers[i+1] = offset
        if numbers[i+1] is None:
            numbers[i+1] = numbers[i]

    return numbers[-1]

if __name__ == '__main__':
    print("Day 5: If You Give A Seed A Fertilizer\n")

    for filename in ["day5_example.txt", "day5_input.txt"]:
        print(f"\nProcessing {filename}")

        with open(filename, 'r') as file:
            lines = file.readlines()
            lines = list(map(lambda x: x.strip(), lines))
            lines = list(filter(lambda x: x != '', lines))

        seeds_simple = get_seeds(lines[0])
        almanac = get_almanac(lines[1:])
        locations = []
        paths = [
            'soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location'
        ]

        for seed in seeds_simple:
            locations.append(get_destination_from_start_position(seed, almanac, paths))

        print('Lowest location number for initial seeds: ' + str(min(locations)))

        seed_ranges = get_seed_ranges(lines[0])
        reversed_almanac = get_almanac(lines[1:], reverse=True)
        locations = []
        reversed_paths = paths[::-1]

        found = False
        location_number = 1 

        # This is WAAAAY better than generating all massive ranges of seeds and going through all them...
        # We're going to go through all locations and reverse the path until we find a seed that is in the
        # seed ranges.
        while not found:
            seed_found = get_destination_from_start_position(location_number, reversed_almanac, reversed_paths)
            if seed_in_ranges(seed_found, seed_ranges):
                found = True
            location_number += 1

        print('Lowest location number for range of seeds: ' + str(location_number-1))