from deck import generate_deck, shuffle_deck, card_str, deal_tableau


def pretty_print_tableau(piles):
    for i, p in enumerate(piles, 1):
        print(f"Pile {i} ({len(p)} cards): ", end='')
        print(' '.join(card_str(c) for c in p))


def main():
    d = generate_deck()
    d = shuffle_deck(d)
    piles, stock = deal_tableau(d)
    pretty_print_tableau(piles)
    print(f"\nStock: {len(stock)} cards")


if __name__ == '__main__':
    main()
