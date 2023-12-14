from functools import reduce

def get_times_and_distances(lines):
    times, distances = [], []
    for i in range(len(lines)):
        clean_line = lines[i].split(":")[1].strip().split(" ")
        clean_line = list(filter(lambda x: x != '', clean_line))
        clean_line = list(map(int, clean_line))
        if i == 0:
            times = clean_line
        else:
            distances = clean_line
    return times, distances

def get_time_and_distance_without_spaces(lines):
    times, distances = [], []
    for i in range(len(lines)):
        clean_line = lines[i].split(":")[1].strip().split(" ")
        clean_line = list(filter(lambda x: x != '', clean_line))
        if i == 0:
            times = clean_line
        else:
            distances = clean_line
    return int(''.join(times)), int(''.join(distances))

def process_race(time, distance):
    possible_races = []
    for i in range(1, time):
        possible_races.append( i*(time-i) )
    ways_to_win = [i for i in possible_races if i>distance]
    return ways_to_win

if __name__ == '__main__':
    print("Day 6: Wait For It")

    for filename in ["day6_example.txt", "day6_input.txt"]:
        print(f"\nProcessing {filename}")

        with open(filename, 'r') as file:
            lines = file.readlines()
        
        times, distances = get_times_and_distances(lines)

        number_of_ways_to_win = []
        for i in range(len(times)):
            ways_to_win = process_race(times[i], distances[i])
            number_of_ways_to_win.append(len(ways_to_win))

        margin_of_error = reduce((lambda x, y: x * y), number_of_ways_to_win)
        print("Margin of errror: " + str(margin_of_error))

        print("\nPart two\n")
        time, distance = get_time_and_distance_without_spaces(lines)
        
        number_of_ways_to_win = []
        ways_to_win = process_race(time, distance)

        print("Margin of errror: " + str(len(ways_to_win)))