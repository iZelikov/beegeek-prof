from datetime import date, time, datetime, timedelta


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
