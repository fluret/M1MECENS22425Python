def f(my_list=None):
    if my_list is None:
        my_list = []
    my_list.append('###')
    return my_list


print(f())
print(f())
print(f())
print(f())
print(f())
print(f(['foo', 'bar', 'baz']))
print(f([1, 2, 3, 4, 5]))
