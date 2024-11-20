import requests

response = requests.get('https://www.example.com')
print(response.status_code)


data = {'key1': 'value1', 'key2': 'value2'}
response = requests.post('https://www.example.com', data=data)
print(response.text)


data = {'key1': 'new_value1', 'key2': 'new_value2'}
response = requests.put('https://www.example.com', data=data)
print(response.text)

response = requests.delete('https://www.example.com')
print(response.status_code)



#  С помощью библиотеки requests я могу использовать различные методы НТТР, такие как
#  GET, POST, PUT, DELETE и другие. Это позволяет мне выполнять различные операции на веб-серверах, такие как получение
# данных, отправка данных, обновление данных и удаление данных.