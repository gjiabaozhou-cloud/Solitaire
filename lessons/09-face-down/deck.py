from typing import List, Tuple
import random

# For this lesson, a Card is (rank, suit, face_up)
Card = Tuple[str, str, bool]

RANKS = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
SUITS = ['♠','♥','♦','♣']


def make_card(rank: str, suit: str, face_up: bool = False) -> Card:
    return (rank, suit, face_up)


def card_str(card: Card) -> str:
    r, s, up = card
    return f"{r}{s}" if up else "XX"


def generate_deck(face_up=False) -> List[Card]:
    return [make_card(rank, suit, face_up) for suit in SUITS for rank in RANKS]


def shuffle_deck(deck: List[Card]) -> List[Card]:
    new_deck = deck.copy()
    random.shuffle(new_deck)
    return new_deck


def deal_tableau(deck: List[Card]):
    piles = []
    offset = 0
    for i in range(7):
        count = i + 1
        pile = deck[offset:offset + count]
        # mark only top as face-up
        pile = [(r, s, False) for (r, s, _) in pile]
        if pile:
            r, s, _ = pile[-1]
            pile[-1] = (r, s, True)
        piles.append(pile)
        offset += count
    return piles, deck[offset:]
