from collections import defaultdict
from functools import total_ordering

@total_ordering
class Rule:
    def __init__(self, node, before_list):
        self.node = node
        self.before_list = before_list

    def __lt__(self, other):
        return self.node in other.before_list

    def __eq__(self, other):
        return self.node == other.node


def get_data(lines):
    rules = defaultdict(list)
    updates = []
    in_rules_part = True
    for line in lines:
        if line.strip() == '':
            in_rules_part = False
            continue
        if in_rules_part:
            before, after = line.strip().split("|")
            rules[int(after)].append(int(before))
        else:
            updates.append([int(x) for x in line.strip().split(",")])
    return rules, updates

def get_valid_invalid_updates(rules, updates):
    valid, invalid = [], []
    for update in updates:
        if all(update[i] in rules[update[i+1]] for i in range(len(update)-1)):
            valid.append(update)
        else:
            invalid.append(update)
    return valid, invalid

def get_middle_pages(valid_updates):
    return [ update[len(update)//2] for update in valid_updates ]

def fix_invalid_updates(rules, invalid_updates):
    sorted_updates = []
    for update in invalid_updates:
        magic_rule_list = []
        for element in update:
            magic_rule_list.append(Rule(element, rules[element]))
        sorted_updates.append(
            [item.node for item in sorted(magic_rule_list)]
        )
    return sorted_updates

if __name__ == '__main__':
    print("Day 5: Print Queue\n")

    print("Example solutions:\n")
    with open("day5_example.txt", 'r') as file:
        page_ordering_rules, updates = get_data(file.readlines())
    valid_updates, invalid_updates = get_valid_invalid_updates(page_ordering_rules, updates)
    print("Sum of middle page numbers: " + str(sum(get_middle_pages(valid_updates))))
    fixed_updates = fix_invalid_updates(page_ordering_rules, invalid_updates)
    print("Sum of fixed middle page numbers: " + str(sum(get_middle_pages(fixed_updates))))

    print("\nInput solutions:\n")
    with open("day5_input.txt", 'r') as file:
        page_ordering_rules, updates = get_data(file.readlines())
    valid_updates, invalid_updates = get_valid_invalid_updates(page_ordering_rules, updates)
    print("Sum of middle page numbers: " + str(sum(get_middle_pages(valid_updates))))
    fixed_updates = fix_invalid_updates(page_ordering_rules, invalid_updates)
    print("Sum of fixed middle page numbers: " + str(sum(get_middle_pages(fixed_updates))))
