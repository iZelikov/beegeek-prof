from datetime import date  # Вставить перед каждым ответом


def today_date():
    print(date.today())


def andrew_day():
    hurricane_andrew = date(1992, 8, 24)
    print(hurricane_andrew.weekday())


def early_hurricanes_count(florida_hurricane_dates: list):
    # счетчик для нужного количества ураганов
    early_hurricanes = 0
    # цикл по датам в которые был ураган
    for hurricane in florida_hurricane_dates:
        # если месяц урагана меньше чем июнь (порядковый номер 6)
        if hurricane.month < 6:
            early_hurricanes += 1
    print(early_hurricanes)


def quartals():
    dates = [date(2010, 9, 28), date(2017, 1, 13), date(2009, 12, 25), date(2010, 2, 27), date(2021, 10, 11),
             date(2020, 3, 13), date(2000, 7, 7), date(1999, 4, 14), date(1789, 11, 19), date(2013, 8, 21),
             date(1666, 6, 6), date(1968, 5, 26)]

    for d in dates:
        print(f'{d.year}-Q{(d.month + 2) // 3}')


def get_min_max(dates: list) -> tuple:
    return (min(dates), max(dates)) if dates else tuple()


def get_date_range(start: date, end: date) -> list:
    dates = []
    for d in range(start.toordinal(), end.toordinal() + 1):
        dates.append(date.fromordinal(d))
    return dates


def saturdays_between_two_dates(start: date, end: date) -> int:
    return sum(date.fromordinal(d).weekday() == 5 for d in
               range(min(start.toordinal(), end.toordinal()), max(start.toordinal(), end.toordinal()) + 1))
