from typing import List, Tuple, Dict
from deck import generate_deck, shuffle_deck, deal_tableau

Card = Tuple[str, str]


def setup_game(shuffle=True) -> Dict:
    deck = generate_deck()
    if shuffle:
        deck = shuffle_deck(deck)
    tableau, stock = deal_tableau(deck)
    return {
        'tableau': tableau,
        'stock': stock,
        'waste': []
    }


def can_place_on_tableau(moving: Card, target: Card) -> bool:
    order = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    mr, ms = moving
    tr, ts = target
    if order.index(mr) != order.index(tr) - 1:
        return False
    red = ('♥', '♦')
    return (ms in red) != (ts in red)


def move_tableau_to_tableau(state: Dict, src_idx: int, depth: int, dst_idx: int) -> Dict:
    src = state['tableau'][src_idx]
    moving_stack = src[depth:]
    if not moving_stack:
        return state.copy()
    target = state['tableau'][dst_idx]
    # if target empty, only king
    if not target:
        if moving_stack[0][0] != 'K':
            return state.copy()
    else:
        if not can_place_on_tableau(moving_stack[0], target[-1]):
            return state.copy()
    new_tableau = [p[:] for p in state['tableau']]
    new_tableau[src_idx] = src[:depth]
    new_tableau[dst_idx] = new_tableau[dst_idx] + moving_stack
    return {'tableau': new_tableau, 'stock': state['stock'], 'waste': state['waste']}
