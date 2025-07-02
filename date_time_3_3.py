from datetime import date, time, datetime


def hospital():
    text = 'Уважаемый пациент, доктор готов принять Вас 15.07.2022 в 08:30'
    dt = datetime.strptime(text, 'Уважаемый пациент, доктор готов принять Вас %d.%m.%Y в %H:%M')
    print(dt)


def timestamp_to_from():
    seconds = 2483228800
    dt = datetime(2011, 11, 4)

    print(datetime.fromtimestamp(seconds))
    print(dt.timestamp())


def am_pm(times_of_purchases: list):
    f = list(filter(lambda x: x.hour < 12, times_of_purchases))
    print(("До полудня", "После полудня")[len(f) < len(times_of_purchases) / 2])


def combine_dates_times(dates: list, times: list):
    print(*sorted(map(datetime.combine, dates, times), key=lambda dt: dt.second), sep='\n')


def fast_homework(data: dict):
    print(
        min(
            data.items(),
            key=lambda x:
            datetime.strptime(x[1][1], '%d.%m.%Y %H:%M:%S').timestamp() -
            datetime.strptime(x[1][0], '%d.%m.%Y %H:%M:%S').timestamp()
        )[0]
    )


def astro_diary(file_name: str) -> str:
    with open(file_name, encoding='utf-8') as diary:
        notes = diary.read().split('\n\n')
    notes.sort(key=lambda s: datetime.strptime(s[:17], '%d.%m.%Y; %H:%M'))
    return "\n\n".join(notes)


def is_available_date(booked_dates: list, date_for_booking: str):
    def parse_date(date_s):
        return datetime.strptime(date_s, '%d.%m.%Y').toordinal()

    def dates_to_range(dates_str):
        if '-' in dates_str:
            dd = dates_str.split('-')
            return range(parse_date(dd[0]), parse_date(dd[1]) + 1)
        else:
            return [parse_date(dates_str)]

    def compare_ranges(range_list, range_to_compare):
        for unavailable in range_list:
            for desired in range_to_compare:
                if desired in unavailable:
                    return False
        return True

    booked_dates_range = map(dates_to_range, booked_dates)
    desired_range = dates_to_range(date_for_booking)
    return compare_ranges(booked_dates_range, desired_range)

