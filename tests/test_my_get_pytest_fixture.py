from pytest import fixture
from python_academy_on_testing.my_get import my_get


@fixture()
def my_beautiful_list():
    return ['a', 'b', 'c']


def test_get(my_beautiful_list):
    element = my_get(lst=my_beautiful_list, index=2, default='z')
    assert element == 'c'


def test_missing_element(my_beautiful_list):
    element = my_get(lst=my_beautiful_list, index=42, default='z')
    assert element == 'z'


def test_removed_element(my_beautiful_list):
    my_beautiful_list.remove('c')
    assert len(my_beautiful_list) == 2
    element = my_get(lst=my_beautiful_list, index=2, default='z')
    assert element == 'z'


def test_the_element_is_still_here(my_beautiful_list):
    # In practice, this test is useless (it is the same as the first one).
    # It is just here to demonstrate that ``my_beautiful_list`` is NOT shared by all the tests.
    element = my_get(lst=my_beautiful_list, index=2, default='z')
    assert element == 'c'


def test_tuple():
    # Notice that some tests may not use the fixture.
    assert my_get(lst=('a', 'b', 'c'), index=1) == 'b'
