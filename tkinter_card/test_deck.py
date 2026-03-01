from deck import generate_deck, shuffle_deck, card_str, draw_top


def test_generate_deck():
    d = generate_deck()
    assert len(d) == 52, "Deck should have 52 cards"
    assert len({card_str(c) for c in d}) == 52, "All cards must be unique"


def test_shuffle_changes_order():
    d = generate_deck()
    before = [card_str(c) for c in d]
    s = shuffle_deck(d)
    after = [card_str(c) for c in s]
    # It's possible shuffle returns same order by chance; assert that at least one position changed
    assert any(a != b for a, b in zip(before, after)), "Shuffle should change order (very likely)"


def test_draw_top():
    d = generate_deck()
    top, rest = draw_top(d)
    assert card_str(top) == card_str(d[0])
    assert len(rest) == 51


if __name__ == '__main__':
    test_generate_deck()
    test_shuffle_changes_order()
    test_draw_top()
    print('All tests passed')
