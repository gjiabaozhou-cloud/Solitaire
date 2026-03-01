from game_model import setup_game, deal_from_stock


def test_setup_game():
    s = setup_game()
    assert 'tableau' in s and 'stock' in s and 'waste' in s
    assert len(s['tableau']) == 7


def test_deal_from_stock():
    s = setup_game()
    original_stock_len = len(s['stock'])
    s2 = deal_from_stock(s)
    assert len(s2['stock']) == original_stock_len - 1
    assert len(s2['waste']) == 1


if __name__ == '__main__':
    test_setup_game()
    test_deal_from_stock()
    print('game_model tests passed')
