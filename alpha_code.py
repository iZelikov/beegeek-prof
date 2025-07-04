from calendar import *
from datetime import date

year = int(input())
[print(date(year, m, (3 - monthrange(year, m)[0]) % 7 + 15).strftime('%d.%m.%Y')) for m in range(1, 13)]
