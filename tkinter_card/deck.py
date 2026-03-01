from typing import List, Tuple
import random

Card = Tuple[str, str]

RANKS = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
SUITS = ['♠','♥','♦','♣']


def make_card(rank: str, suit: str) -> Card:
    """Create an immutable card represented as a (rank, suit) tuple."""
    return (rank, suit)


def card_str(card: Card) -> str:
    return f"{card[0]}{card[1]}"


def generate_deck() -> List[Card]:
    """Return a new ordered list of 52 cards (as tuples)."""
    return [make_card(rank, suit) for suit in SUITS for rank in RANKS]


def shuffle_deck(deck: List[Card]) -> List[Card]:
    """Return a new list with the cards shuffled (pure function).

    Does not mutate the input `deck`.
    """
    new_deck = deck.copy()
    random.shuffle(new_deck)
    return new_deck


def draw_top(deck: List[Card]):
    """Return (top_card, remaining_deck). Raises IndexError if empty."""
    if not deck:
        raise IndexError('draw from empty deck')
    return deck[0], deck[1:]


if __name__ == "__main__":
    d = generate_deck()
    print(len(d), [card_str(c) for c in d[:5]])
