"""Lesson 06 deck: local copy for the game-model lesson."""
from typing import List, Tuple
import random

Card = Tuple[str, str]

RANKS = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
SUITS = ['♠','♥','♦','♣']


def make_card(rank: str, suit: str) -> Card:
    return (rank, suit)


def card_str(card: Card) -> str:
    return f"{card[0]}{card[1]}"


def generate_deck() -> List[Card]:
    return [make_card(rank, suit) for suit in SUITS for rank in RANKS]


def shuffle_deck(deck: List[Card]) -> List[Card]:
    new_deck = deck.copy()
    random.shuffle(new_deck)
    return new_deck


def draw_top(deck: List[Card]):
    if not deck:
        raise IndexError('draw from empty deck')
    return deck[0], deck[1:]


def draw_many(deck: List[Card], n: int):
    if n < 0:
        raise ValueError('n must be >= 0')
    if n > len(deck):
        raise IndexError('not enough cards to draw')
    return deck[:n], deck[n:]


def cut_deck(deck: List[Card], index: int) -> List[Card]:
    if not (0 <= index <= len(deck)):
        raise IndexError('cut index out of range')
    return deck[index:] + deck[:index]


def deal_tableau(deck: List[Card]):
    piles: List[List[Card]] = []
    offset = 0
    for i in range(7):
        count = i + 1
        piles.append(deck[offset:offset + count])
        offset += count
    return piles, deck[offset:]
