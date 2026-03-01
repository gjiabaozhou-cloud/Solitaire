from dataclasses import dataclass
from typing import List
import random


@dataclass(frozen=True)
class Card:
    rank: str
    suit: str

    def __str__(self) -> str:
        return f"{self.rank}{self.suit}"


RANKS = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
SUITS = ['♠','♥','♦','♣']


def generate_deck() -> List[Card]:
    """Return a new ordered list of 52 Card objects."""
    return [Card(rank, suit) for suit in SUITS for rank in RANKS]


def shuffle_deck(deck: List[Card]) -> None:
    """Shuffle a deck in-place."""
    random.shuffle(deck)


if __name__ == "__main__":
    d = generate_deck()
    print(len(d), d[:5])
