from zipfile import ZipFile
import io
import sys
import os
from functools import wraps
# from remember_2_1 import *
# from remember_2_2 import *
# from date_time_3_1 import *
# from date_time_3_2 import *
# from date_time_3_3 import *
# from date_time_3_4 import *
# from date_time_3_5 import *
# from date_time_3_7 import *
# from files_4_2 import *
# from files_4_3 import *
# from collections_6_5 import *
# from collections_6_6 import *
# from collections_6_7 import *
# from collections_6_8 import *
# from collections_6_10 import *
# from exceptions_7_3 import *
# from exceptions_7_4 import *
# from exceptions_7_5 import *
# from recursion_8_2 import *
# from recursion_8_3 import *
# from recursion_8_4 import *
# from funvtions_9_1 import *
# from funvtions_9_2 import *
from funvtions_9_3 import *

import time
from functools import wraps


def timer(func):
    """Декоратор для измерения времени выполнения функции."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()  # Начальное время
        result = func(*args, **kwargs)  # Вызов целевой функции
        end_time = time.perf_counter()  # Конечное время
        elapsed_time = end_time - start_time  # Вычисление затраченного времени

        # Вывод результата в секундах с округлением до 4 знаков
        print(f"Функция {func.__name__!r} выполнилась за {elapsed_time:.4f} секунд")
        return result

    return wrapper


def get_latest_file(folder_path='', ext='zip'):
    files = os.listdir(folder_path)  # Получаем список файлов в каталоге
    # Переменные для хранения информации о файле с самой свежей датой модификации
    latest_file = None
    latest_date = None
    # Бежим по файлам
    for file in files:
        file_path = os.path.join(folder_path, file)
        if file.lower().endswith(ext):  # Если файл с расширением zip
            file_date = os.path.getmtime(file_path)  # Получаем дату модификации файла
            # Если это первый файл или дата модификации текущего файла больше, чем у предыдущего
            if latest_date is None or file_date > latest_date:
                latest_date = file_date
                latest_file = file
    return latest_file


def test(test_number=None):
    dir_path = r'./tests'
    file_name = f"tests_{test_number}.zip" if test_number else get_latest_file(dir_path)
    with ZipFile(f'{dir_path}/{file_name}', 'r') as zip_file:
        total_tests = int(len(zip_file.infolist()) / 2)  # Общее количество тестов
        tests_passed = 0  # Количество пройденных тестов
        print('Архив с тестами:', '\033[1;38;05;129m', file_name, '\033[m')
        for i in range(1, total_tests + 1):
            # Открыть файлы с тестом и ответом
            with zip_file.open(f'{i}', 'r') as t, \
                    zip_file.open(f'{i}.clue', 'r') as a:
                t = t.read().decode('utf-8')  # Содержимое файла Теста
                a = a.read().decode('utf-8')  # Содержимое файла Ответа
                print(f'\033[1;33mtest No {i}\033[m')
                output = io.StringIO()  # Создаем объект для перехвата вывода
                sys.stdout = output  # Перенаправляем стандартный вывод на объект перехвата
                exec(t)  # Выполнить файл с тестом, всегда вернет None
                answer = output.getvalue().rstrip('\n')  # Получаем данные, которые были напечатаны
                sys.stdout = sys.__stdout__  # Возвращаем стандартный вывод на место
                print('etalon: ', '\033[1;34m', a, '\033[m')  # выводим ответ
                print('answer: ', '\033[1;32m' if answer == a else '\033[1;31m', answer, '\033[m')
                if answer == a:
                    tests_passed += 1
                else:
                    print('\033[1;35m', t, '\033[m', sep='')
                print()
        print(' Итого тестов:'.ljust(18), '\033[1;3;34m', total_tests, '\033[m')
        print(' Пройдено тестов:'.ljust(18), '\033[1;3;32m' if total_tests == tests_passed else '\033[31m',
              tests_passed,
              '\033[m')


test()
