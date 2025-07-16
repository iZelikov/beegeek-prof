def month_name():
    try:
        print({1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
               9: 'September', 10: 'October', 11: 'November', 12: 'December'}[int(input())])
    except ValueError:
        print('Введено некорректное значение')
    except KeyError:
        print('Введено число из недопустимого диапазона')


def add_to_list_in_dict(data, key, element):
    try:
        data[key].append(element)
    except:
        data[key] = [element]


def open_file():
    try:
        with open(input(), 'r', encoding='utf-8') as file:
            print(file.read())
    except:
        print("Файл не найден")
