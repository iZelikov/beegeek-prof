from datetime import date, time


def alarm_str():
    alarm = time(7, 30, 25)
    print('Часы:', alarm.strftime('%H'))
    print('Минуты:', alarm.strftime('%M'))
    print('Секунды:', alarm.strftime('%S'))


def birthday_str():
    birthday = date(1992, 10, 6)
    print('Название месяца:', birthday.strftime('%B'))
    print('Название дня недели:', birthday.strftime('%A'))
    print('Год:', birthday.strftime('%Y'))
    print('Месяц:', birthday.strftime('%m'))
    print('День:', birthday.strftime('%d'))


def florida_hurricanes(florida_hurricane_dates):
    # присваиваем самую раннюю дату урагана в переменную first_date
    first_date = min(florida_hurricane_dates)
    # конвертируем дату в ISO и RU формат
    iso = 'Дата первого урагана в ISO формате: ' + first_date.isoformat()
    ru = 'Дата первого урагана в RU формате: ' + first_date.strftime('%d.%m.%Y')
    us = 'Дата первого урагана в US формате: ' + first_date.strftime('%m/%d/%Y')

    print(iso)
    print(ru)
    print(us)


def andrew_hurricane():
    andrew = date(1992, 8, 24)
    print(andrew.strftime('%Y-%m'))  # выводим дату в формате YYYY-MM
    print(andrew.strftime('%B (%Y)'))  # выводим дату в формате month_name (YYYY)
    print(andrew.strftime('%Y-%j'))  # выводим дату в формате YYYY-day_number


def two_dates():
    print(min(date.fromisoformat(input()), date.fromisoformat(input())).strftime('%d-%m (%Y)'))


def sorted_dates():
    print(*(s.strftime('%d/%m/%Y') for s in sorted(date.fromisoformat(input()) for _ in range(int(input())))), sep="\n")


def print_good_dates(dates: list):
    [print(d.strftime('%B %d, %Y')) for d in sorted(dates) if d.year == 1992 and d.month + d.day == 29]


def is_correct(day: int, month: int, year: int) -> bool:
    try: return bool(date(year, month, day))
    except: return False


def all_correct():
    l = [("Некорректная", "Корректная")[is_correct(*map(int, s.split('.')))] for s in iter(input,'end')]
    print(*l, l.count("Корректная"), sep="\n")
