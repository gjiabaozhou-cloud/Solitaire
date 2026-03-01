"""A small functional solitaire model for Lesson 06.

This is a minimal starting point: `setup_game(deck)` returns a dict with
`tableau` (list of lists), `stock`, and `waste`.

All functions return new data (do not mutate inputs).
"""
from typing import List, Tuple, Dict
from deck import generate_deck, shuffle_deck, deal_tableau, draw_top

Card = Tuple[str, str]


def setup_game(deck: List[Card] = None) -> Dict:
    if deck is None:
        deck = shuffle_deck(generate_deck())
    tableau, stock = deal_tableau(deck)
    return {
        'tableau': tableau,
        'stock': stock,
        'waste': []
    }


def deal_from_stock(state: Dict):
    """Deal one card from stock to waste; return new state."""
    if not state['stock']:
        return state.copy()
    top, new_stock = draw_top(state['stock'])
    new_state = {
        'tableau': state['tableau'],
        'stock': new_stock,
        'waste': state['waste'] + [top]
    }
    return new_state
