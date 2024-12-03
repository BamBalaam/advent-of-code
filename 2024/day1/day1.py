def clean_and_separate_lists(lists):
    clean_lists = [line.strip().split("   ") for line in lists]
    left_list, right_list = map(list, zip(*clean_lists))
    left_list = list(map(int, left_list))
    right_list = list(map(int, right_list))
    return left_list, right_list

def calculate_distances(left_list, right_list):
    distances = list(map(lambda x, y: abs(x-y), sorted(left_list), sorted(right_list)))
    return distances

def calculate_similarity_scores(left_list, right_list):
    scores = list(map(lambda x, y: x * right_list.count(x), left_list, right_list))
    return scores


if __name__ == '__main__':
    print("Day 1: Historian Hysteria\n")

    print("Example solutions:\n")
    with open("day1_example.txt", 'r') as file:
        lines = file.readlines()
    left_list, right_list = clean_and_separate_lists(lines)
    distances = calculate_distances(left_list, right_list)
    print("Sum of distances: " + str(sum(distances)))
    scores = calculate_similarity_scores(left_list, right_list)
    print("Total similarity score: " + str(sum(scores)))

    print("\nInput solutions:\n")
    with open("day1_input.txt", 'r') as file:
        lines = file.readlines()
    left_list, right_list = clean_and_separate_lists(lines)
    distances = calculate_distances(left_list, right_list)
    print("Sum of distances: " + str(sum(distances)))
    scores = calculate_similarity_scores(left_list, right_list)
    print("Total similarity score: " + str(sum(scores)))
