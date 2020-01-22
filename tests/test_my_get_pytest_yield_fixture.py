import os
from pytest import yield_fixture
from python_academy_on_testing.my_get import my_get


@yield_fixture()
def my_fid():
    # Setup: done before every test using this fixture. Example: connect to a database, a file...
    fid = open(os.path.join(os.path.dirname(__file__), 'my_file.txt'))

    # The ``return`` is replaced by a ``yield``.
    yield fid

    # Teardown: done after every test using this fixture. Example: disconnect from the database, the file...
    fid.close()


def test_get(my_fid):
    my_beautiful_list = []
    for line in my_fid:
        assert line[0] in {'a', 'b', 'c'}
        my_beautiful_list.append(line[0])
    assert my_get(lst=my_beautiful_list, index=2, default='z') == 'c'
    assert my_get(lst=my_beautiful_list, index=42, default='z') == 'z'
