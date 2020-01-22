import pytest
from python_academy_on_testing.my_get import my_get


def test():
    with pytest.raises(TypeError):
        my_beautiful_list = ['a', 'b', 'c']
        element = my_get(lst=my_beautiful_list, index='some string', default='z')


def test_error_message():
    with pytest.raises(TypeError) as excinfo:
        my_beautiful_list = ['a', 'b', 'c']
        element = my_get(lst=my_beautiful_list, index='some string', default='z')
    excinfo.match('list indices must be integers or slices')
