from datetime import date, time, datetime, timedelta


def delta_time():
    dt = datetime(2021, 11, 4, 13, 6) + timedelta(weeks=1, hours=12)
    print(dt.strftime('%d.%m.%Y %H:%M:%S'))


def days_to_birthday():
    today = date(2021, 11, 4)
    birthday = date(2022, 10, 6)
    days = (birthday - today).days
    print(days)


def day_before_and_after():
    d_format = '%d.%m.%Y'
    d = datetime.strptime(input(), d_format)
    print((d - timedelta(days=1)).strftime(d_format))
    print((d + timedelta(days=1)).strftime(d_format))


def seconds_from_midnight():
    t_format = '%H:%M:%S'
    t_input = datetime.strptime(input(), t_format)
    t_midnight = datetime.strptime('00:00:00', t_format)
    print((t_input - t_midnight).seconds)


def timer_time():
    t_format = '%H:%M:%S'
    t_input = datetime.strptime(input(), t_format)
    delay = int(input())
    print((t_input + timedelta(seconds=delay)).strftime(t_format))


def num_of_sundays(year: int) -> int:
    d1 = datetime(year=year, month=1, day=1).toordinal()
    d2 = datetime(year=year + 1, month=1, day=1).toordinal()
    return len(list(filter(lambda d: datetime.fromordinal(d).weekday() == 6, range(d1, d2))))


def productivity():
    d_format = '%d.%m.%Y'
    d = datetime.strptime(input(), d_format)
    for i in range(1, 11):
        print(d.strftime(d_format))
        d += timedelta(days=i + 1)


def days_between():
    dates = [datetime.strptime(s, '%d.%m.%Y') for s in input().split()]
    print([abs(dates[i + 1] - dates[i]).days for i in range(len(dates) - 1)])


def fill_up_missing_dates(dates_list: list) -> list:
    d_format = '%d.%m.%Y'
    d = sorted(map(lambda date_str: datetime.strptime(date_str, d_format), dates_list))
    return [datetime.fromordinal(i).strftime(d_format) for i in range(d[0].toordinal(), d[-1].toordinal() + 1)]


def rep_po_mateshe():
    t_format = '%H:%M'
    start = datetime.strptime(input().lstrip('0'), t_format)
    finish = datetime.strptime(input().lstrip('0'), t_format)
    while start <= finish - timedelta(minutes=45):
        print(f"{start.strftime(t_format)} - {(start + timedelta(minutes=45)).strftime(t_format)}")
        start += timedelta(minutes=55)
