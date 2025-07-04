from datetime import date, time, datetime, timedelta


def sum_work_time():
    data = [('07:14', '08:46'),
            ('09:01', '09:37'),
            ('10:00', '11:43'),
            ('12:13', '13:49'),
            ('15:00', '15:19'),
            ('15:58', '17:24'),
            ('17:57', '19:21'),
            ('19:30', '19:59')]

    t_f = '%H:%M'
    m = map(lambda dd: datetime.strptime(dd[1], t_f) - datetime.strptime(dd[0], t_f), data)
    print(sum(m, start=timedelta(seconds=0)).seconds // 60)


def friday_13():
    days = {}
    for y in range(1, 10000):
        for m in range(1, 13):
            week_day = date(y, m, 13).weekday()
            days[week_day] = days.get(week_day, 0) + 1

    print(*map(lambda x: x[1], sorted(days.items())), sep="\n")

def shop():
    d_format = '%d.%m.%Y %H:%M'
    raspisanie = [(9, 21), (9, 21), (9, 21), (9, 21), (9, 21), (10, 18), (10, 18)]
    d = datetime.strptime(input(), d_format)
    shop_open = d.replace(minute=0, hour=raspisanie[d.weekday()][0])
    shop_close = d.replace(minute=0, hour=raspisanie[d.weekday()][1])

    if shop_open <= d < shop_close:
        shop_close = d.replace(minute=0, hour=raspisanie[d.weekday()][1])
        print((shop_close - d).seconds // 60)
    else:
        print('Магазин не работает')

def clear_condition():
    d_format = '%d.%m.%Y'
    start_date = datetime.strptime(input(), d_format)
    while not (start_date.day + start_date.month) % 2:
        start_date = date.fromordinal(start_date.toordinal() + 1)
    start = start_date.toordinal()
    end = datetime.strptime(input(), d_format).toordinal() + 1
    for d in range(start, end, 3):
        current_date = date.fromordinal(d)
        if current_date.weekday() not in (0, 3):
            print(current_date.strftime(d_format))

def olderman():
    d_format = '%d.%m.%Y'
    n = int(input())
    date_key = lambda x: datetime.strptime(x[2], d_format)
    employees = sorted([input().split() for _ in range(n)], key=date_key)
    l = list(filter(lambda x: x[2] == employees[0][2], employees))
    print(l[0][2], l[0][0], l[0][1]) if len(l) == 1 else print(l[0][2], len(l))

def same_birthday():
    d_format = '%d.%m.%Y'
    n = int(input())
    employees = {}
    for _ in range(n):
        emp = input().split()
        employees.setdefault(emp[2], []).append(emp)
    e1 = sorted(map(lambda x: (len(x[1]), datetime.strptime(x[0], d_format), x[0]), employees.items()), reverse=True)
    e2 = filter(lambda x: x[0] == e1[0][0], e1)
    [print(i[2]) for i in list(e2)[::-1]]

def nearest_birthday():
    d_format = '%d.%m.%Y'
    d1 = datetime.strptime(input(), d_format)
    n = int(input())
    employees = []
    for _ in range(n):
        emp = input().split()
        d2 = datetime.strptime(emp[2], d_format).replace(year=d1.year)
        if 0 < (d2 - d1).days % 365 <= 7:
            employees.append(emp)
    if employees:
        print(*max(employees, key=lambda e: datetime.strptime(e[2], d_format))[:2])
    else:
        print('Дни рождения не планируются')

def fake_news():
    def choose_plural(amount: int, declensions: tuple) -> str:
        p = {1: 0, 2: 1, 3: 1, 4: 1, 11: 2, 12: 2, 13: 2, 14: 2}
        return f'{amount} {declensions[p.get(amount % 100, p.get(amount % 10, 2))]}'

    d_format = '%d.%m.%Y %H:%M'
    dl_str = '08.11.2022 12:00'
    deadline = datetime.strptime(dl_str, d_format)
    current_date = datetime.strptime(input(), d_format)
    if deadline <= current_date:
        print("Курс уже вышел!")
    else:
        remaining_time = deadline - current_date
        days = remaining_time.days
        hours = remaining_time.seconds // 3600
        minutes = remaining_time.seconds % 3600 // 60
        d_str = f"{choose_plural(days, ("день", "дня", "дней"))} " * (days > 0)
        h_str = f"{choose_plural(hours, ("час", "часа", "часов"))}" * (hours > 0)
        and1_str = "и " * (days > 0) * (hours > 0)
        and2_str = " и " * (days == 0) * (hours > 0) * (minutes > 0)
        m_str = f"{choose_plural(minutes, ("минута", "минуты", "минут"))}" * (minutes > 0) * (days == 0)
        print(f"До выхода курса осталось: {d_str}{and1_str}{h_str}{and2_str}{m_str}")
