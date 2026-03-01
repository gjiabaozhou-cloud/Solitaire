from deck import generate_deck, shuffle_deck


def test_generate_deck():
    d = generate_deck()
    assert len(d) == 52, "Deck should have 52 cards"
    assert len({str(c) for c in d}) == 52, "All cards must be unique"


def test_shuffle_changes_order():
    d = generate_deck()
    before = [str(c) for c in d]
    shuffle_deck(d)
    after = [str(c) for c in d]
    # It's possible shuffle returns same order by chance; assert that at least one position changed
    assert any(a != b for a, b in zip(before, after)), "Shuffle should change order (very likely)"


if __name__ == '__main__':
    test_generate_deck()
    test_shuffle_changes_order()
    print('All tests passed')
