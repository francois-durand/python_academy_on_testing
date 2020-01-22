import unittest
from python_academy_on_testing.my_get import my_get


class TestMyGet(unittest.TestCase):

    def test_get(self):
        my_beautiful_list = ['a', 'b', 'c']
        element = my_get(lst=my_beautiful_list, index=2, default='z')
        self.assertEqual(element, 'c')

    def test_missing_element(self):
        my_beautiful_list = ['a', 'b', 'c']
        element = my_get(lst=my_beautiful_list, index=42, default='z')
        self.assertEqual(element, 'z')
