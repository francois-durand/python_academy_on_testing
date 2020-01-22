from python_academy_on_testing.my_get import my_get


def test_get():
    my_beautiful_list = ['a', 'b', 'c']
    element = my_get(lst=my_beautiful_list, index=2, default='z')
    assert element == 'c'


def test_missing_element():
    my_beautiful_list = ['a', 'b', 'c']
    element = my_get(lst=my_beautiful_list, index=42, default='z')
    assert element == 'z'
