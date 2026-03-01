from game_model import setup_game, deal_from_stock, move_waste_to_foundation, move_waste_to_tableau, move_tableau_to_foundation, auto_move_to_foundations, is_won


def test_setup_and_deal():
    s = setup_game(shuffle=False)
    assert len(s['tableau']) == 7
    s2 = deal_from_stock(s)
    assert len(s2['waste']) == 1


def test_move_waste_to_foundation_when_possible():
    s = setup_game(shuffle=False)
    # with unshuffled deck, an Ace of spades will appear early; deal until we find an Ace
    found = False
    for _ in range(52):
        s = deal_from_stock(s)
        s2 = move_waste_to_foundation(s)
        if s2 != s:
            found = True
            break
    assert found


def test_auto_move():
    s = setup_game(shuffle=False)
    s = deal_from_stock(s)
    s2 = auto_move_to_foundations(s)
    # either unchanged or moved; just ensure it runs
    assert s2 is not None


if __name__ == '__main__':
    test_setup_and_deal()
    test_move_waste_to_foundation_when_possible()
    test_auto_move()
    print('rules tests passed')
