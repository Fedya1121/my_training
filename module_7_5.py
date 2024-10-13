import os
import time


for root, dirs, files in os.walk(r'C:\Users\Саша-Федя\PycharmProjects\pythonProject4\.venv\Scripts\madule_7_5.py'):
    for name in files:
        filepath = os.path.join(root, name)
        filetime = os.path.getctime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname('.venv')
        print(f'Обнаружен файл: {name}, Путь: {filepath}, Размер: {filesize} байт, Время изменения:'
              f' {formatted_time}, Родительская директория: {parent_dir}')