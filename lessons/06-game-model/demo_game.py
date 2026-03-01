from game_model import setup_game, deal_from_stock
from deck import card_str


def main():
    s = setup_game()
    print('Tableau piles lengths:', [len(p) for p in s['tableau']])
    print('Top cards of each pile:')
    tops = [card_str(p[-1]) if p else '(empty)' for p in s['tableau']]
    print('  ', tops)

    s2 = deal_from_stock(s)
    print('\nAfter dealing one card from stock to waste:')
    print('  stock:', len(s2['stock']), 'waste:', len(s2['waste']))
    if s2['waste']:
        print('  waste top:', card_str(s2['waste'][-1]))


if __name__ == '__main__':
    main()
