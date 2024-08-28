def print_params(a=1, b='Fedya', c=23):
    print(a, b, c)

print_params(5, 'ddder')
print_params(7, None, False)
print_params(26)
print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])


value_list = [1, 'fox', True]
values_dict = {'a': 2, 'b': [4, 5, 6], 'c': False}
print_params(*value_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)

