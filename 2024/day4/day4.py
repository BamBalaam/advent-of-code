from math import floor

def generate_cross_path(word_length):
    range_gap = floor(word_length/2)
    test = [
        [(x, x) for x in range(-range_gap, range_gap+1, 1)],
        [
            (1 , -1), (0, 0), (-1, 1)
        ]
    ]
    return test

def generate_all_possible_classic_paths(word_length):
    horizontal = [
        [(0, y) for y in range(word_length)], [(0, y) for y in range(0,-word_length,-1)]
    ]
    vertical = [
        [(x, 0) for x in range(word_length)], [(x, 0) for x in range(0,-word_length,-1)]
    ]
    diagonals = [
        [(x, x) for x in range(word_length)], [(-x, -x) for x in range(word_length)],
        [(x, -x) for x in range(word_length)], [(-x, x) for x in range(word_length)]
    ]
    return [*horizontal, *vertical, *diagonals]

def get_all_valid_paths(position, max_x, max_y, strategy, word_length):
    if strategy == "classic":
        func_name = "generate_all_possible_classic_paths"
    else:
        func_name = "generate_cross_path"
    paths_from_position = [
        [(position[0]+dx, position[1]+dy) for dx,dy in path]
        for path in globals()[func_name](word_length)
    ]
    valid_paths = [
        path for path in paths_from_position
        if all(0 <= pos[0] < max_x and 0 <= pos[1] < max_y for pos in path)
    ]
    return valid_paths

def find_words(grid, search_word, valid_paths, strategy):
    # two strategies:
    # classic = find word in any path leading from first letter
    # cross = find word which repeats twice diagonally from the middle letter
    count = 0
    if strategy == 'classic':
        for path in valid_paths:
            word = "".join(grid[pos[0]][pos[1]] for pos in path)
            if word == search_word:
                count += 1
    else:
        found_count = 0
        for path in valid_paths:
            word = "".join(grid[pos[0]][pos[1]] for pos in path)
            if word in [search_word, search_word[::-1]]:
                found_count += 1
        if found_count == 2:
            count += 1
    return count

def explore_word_search(grid, search_word, strategy):
    count = 0
    max_y, max_x = len(grid), len(grid[0])
    if strategy not in ['classic', 'cross']:
        raise Exception("Strategy must be either 'classic' or 'cross'.")
    if len(search_word) % 2 != 1 and strategy == 'cross':
        raise Exception("Cross strategy requires a word with uneven number of letters.")
    anchor_letter = search_word[0] if strategy == 'classic' else search_word[floor(len(search_word)/2)]
    for index, line in enumerate(grid):
        anchors_positions_found = [(index, i) for i, x in enumerate(line) if x == anchor_letter]
        for anchor_position in anchors_positions_found:
            valid_paths = get_all_valid_paths(anchor_position, max_x, max_y, strategy, len(search_word))
            count += find_words(grid, search_word, valid_paths, strategy)
    return count

def create_grid(lines):
    return [list(line.strip()) for line in lines]

if __name__ == '__main__':
    print("Day 4: Ceres Search\n")

    print("Example solutions:\n")
    with open("day4_example.txt", 'r') as file:
        input_grid = create_grid(file.readlines())
    words_found = explore_word_search(input_grid, "XMAS", "classic")
    print("Number of XMAS: " + str(words_found))
    words_found = explore_word_search(input_grid, "MAS", "cross")
    print("Number of X-MAS: " + str(words_found))

    print("\nInput solutions:\n")
    with open("day4_input.txt", 'r') as file:
        input_grid = create_grid(file.readlines())
    words_found = explore_word_search(input_grid, "XMAS", "classic")
    print("Number of XMAS: " + str(words_found))
    words_found = explore_word_search(input_grid, "MAS", "cross")
    print("Number of X-MAS: " + str(words_found))
