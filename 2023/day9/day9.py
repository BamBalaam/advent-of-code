from functools import reduce

def extrapolate_forwards(sequences):
    last_sequence = max(sequences.keys())
    for i in range(last_sequence, 0, -1):
        expanded_value = sequences[i][-1] + sequences[i-1][-1]
        sequences[i-1].append(expanded_value)
    return sequences[0][-1]

def extrapolate_backawards(sequences):
    last_sequence = max(sequences.keys())
    for i in range(last_sequence, 0, -1):
        expanded_value = sequences[i-1][0] - sequences[i][0]
        sequences[i-1].insert(0, expanded_value)
    return sequences[0][0]

def process_history(history):
    sequences = {}
    sequences[0] = history
    last_sequence = 0
    found = False
    while not found:
        new_sequence = []
        for i in range(len(sequences[last_sequence])-1):
            new_sequence.append(sequences[last_sequence][i+1] - sequences[last_sequence][i])
        sequences[last_sequence + 1] = new_sequence
        last_sequence += 1
        if all(v == 0 for v in new_sequence):
            found = True
    return sequences


if __name__ == '__main__':
    print("Day 9: Mirage Maintenance")

    for filename in ["day9_example.txt", "day9_input.txt"]:
        print(f"\nProcessing {filename}")

        with open(filename, 'r') as file:
            lines = file.readlines()
            lines = list(map(lambda x: x.strip(), lines))
            lines = [line.split(' ') for line in lines]
            for i in range(len(lines)):
                lines[i] = list(map(int, lines[i]))

        sequences = []
        for history in lines:
            sequences.append(process_history(history))

        new_values = []
        for item in sequences:
            new_values.append(extrapolate_forwards(item))

        print("Sum of extrapolated values: " + str(reduce((lambda x, y: x + y), new_values)))

        new_values = []
        for item in sequences:
            new_values.append(extrapolate_backawards(item))
        print("Sum of backwards extrapolated values: " + str(reduce((lambda x, y: x + y), new_values)))