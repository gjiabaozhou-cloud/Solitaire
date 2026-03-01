from typing import List, Tuple, Dict
from deck import generate_deck, shuffle_deck, deal_tableau, card_str

# Card is (rank, suit, face_up)
Card = Tuple[str, str, bool]


def setup_game(shuffle=True) -> Dict:
    deck = generate_deck()
    if shuffle:
        deck = shuffle_deck(deck)
    tableau, stock = deal_tableau(deck)
    return {
        'tableau': tableau,  # list of piles (each pile is list of Card)
        'stock': stock,      # remaining cards are face-down in stock
        'waste': []
    }


def move_from_tableau(state: Dict, src_idx: int) -> Dict:
    """Remove top card from tableau[src_idx] and reveal new top if any."""
    new_tableau = [p[:] for p in state['tableau']]
    pile = new_tableau[src_idx]
    if not pile:
        return {'tableau': new_tableau, 'stock': state['stock'], 'waste': state['waste']}
    removed = pile.pop()
    # reveal new top
    if pile:
        r, s, _ = pile[-1]
        pile[-1] = (r, s, True)
    return {'tableau': new_tableau, 'stock': state['stock'], 'waste': state['waste'] + [removed]}


def deal_from_stock(state: Dict) -> Dict:
    if not state['stock']:
        return state.copy()
    top = state['stock'][0]
    return {'tableau': state['tableau'], 'stock': state['stock'][1:], 'waste': state['waste'] + [top]}
