import json
try:
    with open(input(),'r',encoding='utf-8') as file:
        try:
            print(json.load(file))
        except Exception:
            print('Ошибка при десериализации')
except FileNotFoundError:
    print('Файл не найден')