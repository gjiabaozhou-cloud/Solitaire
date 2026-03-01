from deck import generate_deck, card_str


def main():
    d = generate_deck()
    for i, c in enumerate(d, 1):
        print(f"{i:2d}: {card_str(c)}")


if __name__ == '__main__':
    main()
