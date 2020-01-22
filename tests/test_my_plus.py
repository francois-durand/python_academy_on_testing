from python_academy_on_testing.my_plus import my_plus


def test():
    assert my_plus(3, 4) == 7
    assert my_plus('a', 'b') == 'ab'
