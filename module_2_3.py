my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while index < len(my_list):
    element = my_list[index]
    index += 1
    if element > 0:
        print(element)
        continue
    elif element == 0:
        continue
    elif element < 0:
        break

































