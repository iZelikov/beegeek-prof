def get_weekday(number: int) -> str:
    week_day = {1: "Понедельник", 2: "Вторник", 3: "Среда", 4: "Четверг", 5: "Пятница", 6: "Суббота",
                7: "Воскресенье", }
    try:
        if not isinstance(number, int):
            raise TypeError('Аргумент не является целым числом')
        elif not number in range(1, 8):
            raise ValueError('Аргумент не принадлежит требуемому диапазону')
        return week_day[number]
    except Exception as e:
        raise


def get_id(names, name):
    if not isinstance(name, str):
        raise TypeError('Имя не является строкой')
    elif not (name.isalpha() and name.istitle()):
        raise ValueError('Имя не является корректным')
    return len(names) + 1

def json_decode():
    import json
    try:
        with open(input(), 'r', encoding='utf-8') as file:
            try:
                print(json.load(file))
            except json.JSONDecodeError:
                print('Ошибка при десериализации')
    except FileNotFoundError:
        print('Файл не найден')