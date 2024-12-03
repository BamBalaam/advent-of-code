from itertools import pairwise

# Utils

def clean_reports(raw_reports):
    reports = [line.strip().split(" ") for line in raw_reports]
    return [list(map(int, report)) for report in reports]

def check_increasing(input_list):
    return all(x < y for x, y in pairwise(input_list))

def check_decreasing(input_list):
    return all(x > y for x, y in pairwise(input_list))

def check_adjacent_levels(input_list):
    return all(abs(x-y) in [1,2,3] for x, y in pairwise(input_list))

# Calculations

def check_safe(report):
    if check_increasing(report) or check_decreasing(report):
        return check_adjacent_levels(report)
    return False

def check_safe_with_problem_dampener(report):
    if check_safe(report):
        return True
    for i in range(len(report)):
        temp_report = report.copy()
        temp_report.pop(i)
        if check_safe(temp_report):
            return True
    return False

def check_reports(reports):
    return [check_safe(report) for report in clean_reports(reports)]

def check_reports_with_problem_dampener(reports):
    return [check_safe_with_problem_dampener(report) for report in clean_reports(reports)]

if __name__ == '__main__':
    print("Day 2: Red-Nosed Reports\n")

    print("Example solutions:\n")
    with open("day2_example.txt", 'r') as file:
        lines = file.readlines()
    checked_reports = check_reports(lines)
    print("Number of Safe reports: " + str(sum(checked_reports)))
    checked_reports = check_reports_with_problem_dampener(lines)
    print("Number of Safe reports (with Problem Dampener): " + str(sum(checked_reports)))

    print("\nInput solutions:\n")
    with open("day2_input.txt", 'r') as file:
        lines = file.readlines()
    checked_reports = [check_safe(report) for report in clean_reports(lines)]
    print("Number of Safe reports: " + str(sum(checked_reports)))
    checked_reports = check_reports_with_problem_dampener(lines)
    print("Number of Safe reports (with Problem Dampener): " + str(sum(checked_reports)))
