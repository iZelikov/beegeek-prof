import sys
from datetime import date, time, datetime, timedelta


def reverse_line():
    for line in sys.stdin:
        print(line[::-1].strip("\n"))


def date_range():
    dates = []
    for line in sys.stdin:
        dates.append(date.fromisoformat(line.strip("\n")))
    print((max(dates) - min(dates)).days)


def socks_game():
    players = ['Дима', 'Анри']
    game = [int(line.strip()) for line in sys.stdin]
    result = players[(game[-1] % 2 + len(game) % 2) % 2]
    print(result)


def purples_tall():
    tall = [int(line.strip()) for line in open(0)]
    print(f'Рост самого низкого ученика: {min(tall)}',
          f'Рост самого высокого ученика: {max(tall)}',
          f'Средний рост: {sum(tall) / len(tall)}', sep="\n") \
        if tall else print("нет учеников")


def count_comments():
    print(sum(1 for line in open(0) if line.strip()[0] == '#'))

def remove_comments():
    [print(line.rstrip('\n')) for line in open(0) if not line.strip().startswith('#')]

def panorama_pub():
    content = [line.strip().split(' / ') for line in sys.stdin]
    category = content.pop()[0]
    f = sorted(filter(lambda x: x[1] == category, content), key=lambda y: (float(y[2]), y[0]))
    print(*map(lambda z: z[0], f), sep='\n')

def dates_order():
    d_format = '%d.%m.%Y'
    dates = [datetime.strptime(d.strip(), d_format) for d in sys.stdin]
    if dates == sorted(set(dates)):
        print('ASC')
    elif dates == sorted(set(dates), reverse=True):
        print('DESC')
    else:
        print('MIX')

def progression_type():
    prev_prev = int(sys.stdin.readline().strip())
    prev = int(sys.stdin.readline().strip())
    a_n = prev - prev_prev
    g_n = prev / prev_prev
    progressions = ("Не прогрессия", "Арифметическая прогрессия", "Геометрическая прогрессия")
    a, g = 1, 2
    for i in sys.stdin:
        current = int(i.strip())
        if current - prev != a_n: a = 0
        if current / prev != g_n: g = 0
        if not a and not g: break
        prev = current
    print(progressions[a + g])