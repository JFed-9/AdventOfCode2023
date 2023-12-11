from functools import cmp_to_key

best_cards = 'AKQT98765432J'

def getPower(hand):
    unique_cards = set([x for x in hand])
    if 'J' in unique_cards: unique_cards.remove('J')
    jokers = hand.count('J')
    score = 7
    if jokers == 5:
        score = min(score,1)
    if jokers == 4:
        score = min(score,2)
    if jokers == 3:
        if len(unique_cards) == 1:
            score = min(score,3)
        score = min(score,4)
    if jokers == 2:
        if len(unique_cards) == 2:
            score = min(score,5)
        score = min(score,6)
    for ch in unique_cards:
        if hand.count(ch) + jokers == 5:
            score = min(score,1)
            continue
        if hand.count(ch) + jokers == 4:
            score = min(score,2)
            continue
        if hand.count(ch) + jokers == 3:
            if len(unique_cards) == 2:
                score = min(score,3)
                continue
            score = min(score,4)
            continue
        if hand.count(ch) + jokers == 2:
            if len(unique_cards) == 3:
                score = min(score,5)
                continue
            score = min(score,6)
            continue
    return score

def CustomSortComparator(first, second):
    if getPower(first) > getPower(second):  #First is worse
        return -1
    if getPower(first) < getPower(second):  #First is better
        return 1
    i = 0
    while best_cards.find(first[i]) == best_cards.find(second[i]): i+=1
    if best_cards.find(first[i]) < best_cards.find(second[i]):  #First is better
        return 1
    return -1    #First is worse

with open('Day7.txt') as file:
    lines = file.readlines()

hands = []
bids = {}
winnings = 0

for line in lines:
    hand, bid = line.strip().split(' ')
    hands.append(hand)
    bids[hand] = int(bid)

hands.sort(key=cmp_to_key(CustomSortComparator))

for ind, hand in enumerate(hands):
    winnings += (ind + 1) * bids[hand]
    print(f"{hand}: {ind + 1} * {bids[hand]}")

print(f"Winnings: {winnings}")