from features import push_undo, pop_undo


def test_undo_stack():
    s1 = {'a': 1}
    s2 = {'a': 2}
    stack = []
    stack = push_undo(stack, s1)
    stack = push_undo(stack, s2)
    top, stack = pop_undo(stack)
    assert top == s2
    top, stack = pop_undo(stack)
    assert top == s1


if __name__ == '__main__':
    test_undo_stack()
    print('features tests passed')
