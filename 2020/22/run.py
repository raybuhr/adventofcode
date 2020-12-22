from aocd import get_data


def split_cards(data):
    decks = data.split("\n\n")
    cards = {}
    for deck in decks:
        player, hand = deck.split(":")
        cards[player] = [int(card) for card in hand.splitlines() if card != ""]
    return cards


def play_hand(cards):
    p1 = cards["Player 1"].pop(0)
    p2 = cards["Player 2"].pop(0)
    if p1 > p2:
        cards["Player 1"] += [p1, p2]
    else:
        cards["Player 2"] += [p2, p1]


def play_combat(data):
    cards = split_cards(data)
    done = False
    while not done:
        play_hand(cards)
        if len(cards["Player 1"]) == 0 or len(cards["Player 2"]) == 0:
            done = True
    p1, p2 = len(cards["Player 1"]), len(cards["Player 2"])
    if p1 > p2:
        hand = cards["Player 1"]
        ct = p1
    else:
        hand = card["Player 2"]
        ct = p2
    return sum(card * score for card, score in zip(hand, range(ct, 0, -1)))


def play_recursive_combat(cards):
    rd = 1
    p1_seen, p2_seen = [], []
    winner = None
    while not winner:
        p1_hand = ",".join([str(c) for c in cards["Player 1"]])
        p2_hand = ",".join([str(c) for c in cards["Player 2"]])
        if (p1_hand in p1_seen) or (p2_hand in p2_seen):
            winner = "Player 1"
            break
        else:
            p1_seen.append(p1_hand)
            p2_seen.append(p2_hand)
        p1_ct, p2_ct = len(cards["Player 1"]), len(cards["Player 2"])
        if p1_ct == 0:
            winner = "Player 2"
            break
        if p2_ct == 0:
            winner = "Player 1"
            break
        p1 = cards["Player 1"].pop(0)
        p2 = cards["Player 2"].pop(0)
        if (p1_ct - 1 < p1) or (p2_ct - 1 < p2):
            if p1 > p2:
                cards["Player 1"] += [p1, p2]
            else:
                cards["Player 2"] += [p2, p1]
        if (p1_ct - 1 >= p1) and (p2_ct - 1 >= p2):
            subgame = {
                "Player 1": [c for c in cards["Player 1"][:p1]],
                "Player 2": [c for c in cards["Player 2"][:p2]],
            }
            won, _, _ = play_recursive_combat(subgame)
            if won == "Player 1":
                cards[won] += [p1, p2]
            else:
                cards[won] += [p2, p1]
        rd += 1
    return winner, cards[winner], rd


def solve_part_b(data):
    cards = split_cards(data)
    winner, hand, rds = play_recursive_combat(cards)
    score = sum(card * score for card, score in zip(hand, range(len(hand), 0, -1)))
    return score


if __name__ == "__main__":
    data = get_data(year=2020, day=22)
    print("Part 1:")
    print(play_combat(data))
    print("Part 2:")
    print(solve_part_b(data))
