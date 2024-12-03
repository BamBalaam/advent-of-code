def clean_and_separate_lists(lists):
    clean_lists = [line.strip().split("   ") for line in lists]
    left_list, right_list = map(list, zip(*clean_lists))
    return list(map(int, left_list)), list(map(int, right_list))

def calculate_distances(left_list, right_list):
    return list(map(lambda x, y: abs(x-y), sorted(left_list), sorted(right_list)))

def calculate_similarity_scores(left_list, right_list):
    return list(map(lambda x, y: x * right_list.count(x), left_list, right_list))

if __name__ == '__main__':
    print("Day 1: Historian Hysteria\n")

    print("Example solutions:\n")
    with open("day1_example.txt", 'r') as file:
        lines = file.readlines()
    distances = calculate_distances(*clean_and_separate_lists(lines))
    print("Sum of distances: " + str(sum(distances)))
    scores = calculate_similarity_scores(*clean_and_separate_lists(lines))
    print("Total similarity score: " + str(sum(scores)))

    print("\nInput solutions:\n")
    with open("day1_input.txt", 'r') as file:
        lines = file.readlines()
    distances = calculate_distances(*clean_and_separate_lists(lines))
    print("Sum of distances: " + str(sum(distances)))
    scores = calculate_similarity_scores(*clean_and_separate_lists(lines))
    print("Total similarity score: " + str(sum(scores)))
