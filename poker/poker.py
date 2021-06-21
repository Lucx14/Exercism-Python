from typing import List
from collections import Counter

HIGH_CARD = "high card"
PAIR = "pair"
TWO_PAIR = "two pair"
THREE_OF_A_KIND = "three of a kind"
STRAIGHT = "straight"
FLUSH = "flush"
FULL_HOUSE = "full house"
FOUR_OF_A_KIND = "four of a kind"
STRAIGHT_FLUSH = "straight flush"
ROYAL_FLUSH = "royal flush"

RANKS = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
EDGE_STRAIGHT = [12, 3, 2, 1, 0]
HANDS = (
    HIGH_CARD,
    PAIR,
    TWO_PAIR,
    THREE_OF_A_KIND,
    STRAIGHT,
    FLUSH,
    FULL_HOUSE,
    FOUR_OF_A_KIND,
    STRAIGHT_FLUSH,
    ROYAL_FLUSH,
)


def is_sequence(l: List[int]) -> bool:
    if sorted(l) == [0, 1, 2, 3, 12]:
        return True
    return sorted(l) == list(range(min(l), max(l) + 1))


class Card:
    def __init__(self, name):
        self.name = name
        self.suit = name[-1:]
        self.rank = name[:-1]
        self.value = RANKS.index(self.rank)


class Hand:
    def __init__(self, hand, card=Card):
        self.name = hand
        self.cards = [card(c) for c in hand.split()]
        self.ranks = sorted([card.value for card in self.cards], reverse=True)
        self.score = self._score()

    def _groups(self, size):
        return [key for key, value in Counter(self.ranks).items() if value == size]

    def _score(self):
        uniq_suits = len(set(card.suit for card in self.cards))
        uniq_ranks = len(set(self.ranks))

        high_card = self.ranks[0]
        if self.ranks == EDGE_STRAIGHT:
            high_card = 3

        if uniq_suits == 1 and self.ranks == [12, 11, 10, 9, 8]:
            return (HANDS.index(ROYAL_FLUSH), *self.ranks)
        elif uniq_suits == 1 and is_sequence(self.ranks):
            return (HANDS.index(STRAIGHT_FLUSH), high_card)
        elif self._groups(4):
            return (HANDS.index(FOUR_OF_A_KIND), *self._groups(4), *self._groups(1))
        elif uniq_ranks == 2:
            return (HANDS.index(FULL_HOUSE), *self._groups(3), *self._groups(2))
        elif uniq_suits == 1:
            return (HANDS.index(FLUSH), *self.ranks)
        elif is_sequence(self.ranks):
            return (HANDS.index(STRAIGHT), high_card)
        elif self._groups(3) and self._groups(1):
            return (HANDS.index(THREE_OF_A_KIND), *self._groups(3), *self._groups(1))
        elif uniq_ranks == 3:
            return (HANDS.index(TWO_PAIR), *self._groups(2), *self._groups(1))
        elif uniq_ranks == 4:
            return (HANDS.index(PAIR), *self._groups(2), *self._groups(1))
        else:
            return (HANDS.index(HIGH_CARD), *self.ranks)


class Game:
    def __init__(self, hands, hand=Hand):
        self.hands = [hand(h) for h in hands]

    def winning_hands(self):
        """Determine winning hands

        Returns:
            List[str]: Calculates the score of the best hand and then returns all hands that match the max score
        """
        max_score = max(hand.score for hand in self.hands)
        return [hand.name for hand in self.hands if hand.score == max_score]


def best_hands(hands):
    return Game(hands).winning_hands()
