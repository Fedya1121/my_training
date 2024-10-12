import os
import time


for root, dirs, files in os.walk(r'C:\Users\Саша-Федя\PycharmProjects\pythonProject4\.venv\Scripts\madule_7_5.py'):
  for file in files:
    filepath = os.path.join(root, name)
    filetime = os.path.getctime(file_path)
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = os.path.getsize(file_path)
    parent_dir = os.path.dirname('p')
    print(f'Обнаружен файл: {file}, Путь: {filepath},'
          f' Размер: {filesize} байт, Время изменения: {formatted_time},'
          f' Родительская директория: {parent_dir}')