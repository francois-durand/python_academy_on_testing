from python_academy_on_testing.my_get import my_get


my_beautiful_list = ['a', 'b', 'c']
element = my_get(lst=my_beautiful_list, index=2, default='z')
assert element == 'c'
