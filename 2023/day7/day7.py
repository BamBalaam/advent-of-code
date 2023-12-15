from functools import reduce


def score_cards(cards, card_values):
    score = 0
    card_importance_ratio = 5
    for card in cards:
        score += (100 ** card_importance_ratio) * (card_values.index(card))
        card_importance_ratio -= 1
    return score

def hand_rank_helper(hand):
    card_values_normal = '2 3 4 5 6 7 8 9 T J Q K A'.split()
    return score_cards(hand['cards'], card_values_normal)

def hand_rank_helper_jokers(hand):
    card_values_joker = 'J 2 3 4 5 6 7 8 9 T Q K A'.split()
    return score_cards(hand['cards'], card_values_joker)

def classify_hand(cards):
    same_cards = sorted([cards.count(a) for a in set(cards)])
    if len(same_cards) == 1:
        hand_type = 'five_of_a_kind'
    elif len(same_cards) == 2:
        if same_cards == [1, 4]:
            hand_type = 'four_of_a_kind'
        if same_cards == [2, 3]:
            hand_type = 'full_house'
    elif len(same_cards) == 3:
        if same_cards == [1, 1, 3]:
            hand_type = 'three_of_a_kind'
        if same_cards == [1, 2, 2]:
            hand_type = 'two_pair'
    elif len(same_cards) == 4:
        hand_type = 'one_pair'
    elif len(same_cards) == 5:
        hand_type = 'high_card'

    return hand_type

def rank_hands(hands):
    ranked_hands = {
        'five_of_a_kind' : [], 'four_of_a_kind': [], 'full_house': [],
        'three_of_a_kind': [], 'two_pair': [], 'one_pair': [], 'high_card': []
    }

    for hand in hands:
        hand_type = classify_hand(hand['cards'])
        ranked_hands[hand_type].append(hand)

    for hand_type, hands in ranked_hands.items():
        ranked_hands[hand_type] = sorted(hands, key=hand_rank_helper, reverse=True)

    return ranked_hands

def list_of_cards_has_joker(cards_list):
    for cards in cards_list:
        if 'J' in cards:
            return True
    return False

def create_replacement_hands(hand):
    replacement_list = '2 3 4 5 6 7 8 9 T Q K A'. split()
    original_cards = hand['cards']
    replacement_cards = [original_cards]
    while list_of_cards_has_joker(replacement_cards):
        for cards in replacement_cards:
            for i in range(len(cards)):
                if cards[i] == 'J':
                    replacement_cards.remove(cards)
                    for replacement in replacement_list:
                        new_cards = list(cards)
                        new_cards[i] = replacement
                        new_cards = ''.join(new_cards)
                        replacement_cards.append(new_cards)
                    break
    replacement_hands = []
    for cards in replacement_cards:
        replacement_hands.append({
            'cards': cards, 'bid': hand['bid']    
        })
    return replacement_hands

def rank_hands_with_jokers(hands):
    ranked_hands = {
        'five_of_a_kind' : [], 'four_of_a_kind': [], 'full_house': [],
        'three_of_a_kind': [], 'two_pair': [], 'one_pair': [], 'high_card': []
    }

    for hand in hands:
        if 'J' not in hand['cards']:
            hand_type = classify_hand(hand['cards'])
            ranked_hands[hand_type].append(hand)
        else:
            replacement_ranked_hands = {
                'five_of_a_kind' : [], 'four_of_a_kind': [], 'full_house': [],
                'three_of_a_kind': [], 'two_pair': [], 'one_pair': [], 'high_card': []
            }
            replacement_hands = create_replacement_hands(hand)
            ranked_replacement_hands = rank_hands(replacement_hands)
            for key, values in ranked_replacement_hands.items():
                if len(values) != 0:
                    ranked_hands[key].append(hand)
                    break
    for hand_type, hands in ranked_hands.items():
        ranked_hands[hand_type] = sorted(hands, key=hand_rank_helper_jokers, reverse=True)
    return ranked_hands


def get_hands(lines):
    hands = []
    for line in lines:
        line = line.strip()
        cards, bid = line.split(" ")
        hands.append({'cards': cards, 'bid': int(bid)})
    return hands

def calculate_winnings(ranked_hands, number_of_hands):
    total_winnings = 0
    rank_number = number_of_hands
    for key, value in ranked_hands.items():
        for item in value:
            total_winnings += item['bid'] * rank_number
            rank_number -= 1
    return total_winnings

if __name__ == '__main__':
    print("Day 7: Camel Cards")

    for filename in ["day7_example.txt", "day7_input.txt"]:
        print(f"\nProcessing {filename}")

        with open(filename, 'r') as file:
            lines = file.readlines()
        
        hands = get_hands(lines)
        ranked_hands = rank_hands(hands)
        total_winnings = calculate_winnings(ranked_hands, len(hands))
        print("Total Winnings Part 1: " + str(total_winnings))

        ranked_hands = rank_hands_with_jokers(hands)
        total_winnings = calculate_winnings(ranked_hands, len(hands))
        print("Total Winnings Part 2: " + str(total_winnings))