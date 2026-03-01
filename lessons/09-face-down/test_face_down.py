from game_model import setup_game, move_from_tableau, deal_from_stock
from deck import card_str


def test_reveal_on_remove():
    s = setup_game(shuffle=False)
    # tableau piles lengths should be 1..7
    lengths = [len(p) for p in s['tableau']]
    assert lengths == [1,2,3,4,5,6,7]
    # top of pile 3 (index 2) initially face-up
    top = s['tableau'][2][-1]
    assert top[2] is True
    # remove top from pile 2 (index 1) and ensure new top is revealed
    s2 = move_from_tableau(s, 1)
    # after removing one card from pile index 1, its new top (if any) should be face_up
    if s2['tableau'][1]:
        assert s2['tableau'][1][-1][2] is True


def test_deal_from_stock():
    s = setup_game(shuffle=False)
    orig_stock = len(s['stock'])
    s2 = deal_from_stock(s)
    assert len(s2['stock']) == orig_stock - 1
    assert len(s2['waste']) == 1


if __name__ == '__main__':
    test_reveal_on_remove()
    test_deal_from_stock()
    print('face-down tests passed')
