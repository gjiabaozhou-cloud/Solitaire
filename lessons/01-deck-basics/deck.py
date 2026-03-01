"""Minimal deck for Lesson 01: deck basics.

Keep this file tiny so students focus on simple functions.
"""
from typing import List, Tuple

Card = Tuple[str, str]

RANKS = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
SUITS = ['♠','♥','♦','♣']


def make_card(rank: str, suit: str) -> Card:
    return (rank, suit)


def card_str(card: Card) -> str:
    return f"{card[0]}{card[1]}"


def generate_deck() -> List[Card]:
    """Return a new ordered list of 52 cards (as tuples)."""
    return [make_card(rank, suit) for suit in SUITS for rank in RANKS]
