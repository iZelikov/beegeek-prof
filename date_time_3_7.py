from calendar import *
from datetime import date


def leap_years():
    n = int(input())
    [print(isleap(int(input()))) for _ in range(n)]


def month_calendar():
    inp = input().split()
    prmonth(int(inp[0]), list(month_abbr).index(inp[1]))


def month_range():
    print(monthrange(*map(int, input().split()))[1])


def month_name_range():
    y, m = input().split()
    print(monthrange(int(y), list(month_name).index(m))[1])


def get_days_in_month(year, month):
    return [date(year, list(month_name).index(month), d) for d in
            range(1, monthrange(int(year), list(month_name).index(month))[1] + 1)]


def get_all_mondays(year):
    january_1 = monthrange(year, 1)[0]
    first_monday = -january_1 % 7 + 1
    start = date(year, 1, first_monday).toordinal()
    end = date(year, 12, 31).toordinal() + 1
    return [date.fromordinal(d) for d in range(start, end, 7)]

def third_thursday():
    year = int(input())
    [print(date(year, m, (3 - monthrange(year, m)[0]) % 7 + 15).strftime('%d.%m.%Y')) for m in range(1, 13)]
