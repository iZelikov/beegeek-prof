try:
    with open(input(), 'r', encoding='utf-8') as file:
        print(file.read())
except:
    print("Файл не найден")