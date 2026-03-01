from typing import List, Tuple, Dict
from deck import generate_deck, shuffle_deck, deal_tableau, draw_top

Card = Tuple[str, str]


ORDER = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']


def setup_game(shuffle=True) -> Dict:
    deck = generate_deck()
    if shuffle:
        deck = shuffle_deck(deck)
    tableau, stock = deal_tableau(deck)
    return {
        'tableau': tableau,
        'foundations': {s: [] for s in ['♠','♥','♦','♣']},
        'stock': stock,
        'waste': []
    }


def deal_from_stock(state: Dict) -> Dict:
    if not state['stock']:
        return state.copy()
    top, new_stock = draw_top(state['stock'])
    return {
        'tableau': state['tableau'],
        'foundations': state['foundations'],
        'stock': new_stock,
        'waste': state['waste'] + [top]
    }


def can_move_to_foundation(card: Card, foundation: List[Card]) -> bool:
    rank, suit = card
    if not foundation:
        return rank == 'A'
    top_rank = foundation[-1][0]
    return ORDER.index(rank) == ORDER.index(top_rank) + 1


def move_waste_to_foundation(state: Dict) -> Dict:
    if not state['waste']:
        return state.copy()
    card = state['waste'][-1]
    suit = card[1]
    f = state['foundations'][suit]
    if can_move_to_foundation(card, f):
        new_found = {k: v[:] for k, v in state['foundations'].items()}
        new_found[suit].append(card)
        return {
            'tableau': state['tableau'],
            'foundations': new_found,
            'stock': state['stock'],
            'waste': state['waste'][:-1]
        }
    return state.copy()


def can_place_on_tableau(moving: Card, target: Card) -> bool:
    mr, ms = moving
    tr, ts = target
    if ORDER.index(mr) != ORDER.index(tr) - 1:
        return False
    red = ('♥', '♦')
    return (ms in red) != (ts in red)


def move_waste_to_tableau(state: Dict, pile_idx: int) -> Dict:
    if not state['waste']:
        return state.copy()
    moving = state['waste'][-1]
    pile = state['tableau'][pile_idx]
    if not pile:
        if moving[0] == 'K':
            new_tableau = [p[:] for p in state['tableau']]
            new_tableau[pile_idx].append(moving)
            return {'tableau': new_tableau,'foundations': state['foundations'],'stock': state['stock'],'waste': state['waste'][:-1]}
        return state.copy()
    else:
        if can_place_on_tableau(moving, pile[-1]):
            new_tableau = [p[:] for p in state['tableau']]
            new_tableau[pile_idx].append(moving)
            return {'tableau': new_tableau,'foundations': state['foundations'],'stock': state['stock'],'waste': state['waste'][:-1]}
    return state.copy()


def move_tableau_to_tableau(state: Dict, src_idx: int, depth: int, dst_idx: int) -> Dict:
    src = state['tableau'][src_idx]
    moving_stack = src[depth:]
    if not moving_stack:
        return state.copy()
    target = state['tableau'][dst_idx]
    if not target:
        if moving_stack[0][0] != 'K':
            return state.copy()
    else:
        if not can_place_on_tableau(moving_stack[0], target[-1]):
            return state.copy()
    new_tableau = [p[:] for p in state['tableau']]
    new_tableau[src_idx] = src[:depth]
    new_tableau[dst_idx] = new_tableau[dst_idx] + moving_stack
    return {'tableau': new_tableau,'foundations': state['foundations'],'stock': state['stock'],'waste': state['waste']}


def move_tableau_to_foundation(state: Dict, src_idx: int) -> Dict:
    pile = state['tableau'][src_idx]
    if not pile:
        return state.copy()
    card = pile[-1]
    suit = card[1]
    f = state['foundations'][suit]
    if can_move_to_foundation(card, f):
        new_found = {k: v[:] for k, v in state['foundations'].items()}
        new_found[suit].append(card)
        new_tableau = [p[:] for p in state['tableau']]
        new_tableau[src_idx] = pile[:-1]
        return {'tableau': new_tableau,'foundations': new_found,'stock': state['stock'],'waste': state['waste']}
    return state.copy()


def auto_move_to_foundations(state: Dict) -> Dict:
    # attempt waste->foundation
    s = move_waste_to_foundation(state)
    if s != state:
        return s
    # attempt tableau->foundation (for any pile)
    for i in range(len(state['tableau'])):
        s2 = move_tableau_to_foundation(state, i)
        if s2 != state:
            return s2
    return state.copy()


def is_won(state: Dict) -> bool:
    return all(len(f) == 13 for f in state['foundations'].values())
