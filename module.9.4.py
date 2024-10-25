first = 'Мама мыла раму'
second = 'Рамена мало было'
new_list = (list(map(lambda x, y: x == y,first, second)))
print(new_list)


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            file.write(str(data_set[0]) + '\n')
            file.write(str(data_set[1]) + '\n')
            file.write('\n')

    return write_everything
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

with open('example.txt', 'r',encoding='utf-8') as file:
    print(file.read())

import random

class MysticBall:
    def __init__(self, word):
        self.word = word

    def __call__(self):
        return random.choice(self.word)

first_ball = MysticBall(['Да', 'Нет', 'Наверное'])
print(first_ball())
print(first_ball())
print(first_ball())