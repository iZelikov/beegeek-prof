import re

def phones_re():
    import sys
    phones = sys.stdin.read().split('\n')
    regexp = r'(\d+)[- ](\d+)[- ](\d+)'
    for phone in phones:
        match = re.fullmatch(regexp, phone)
        print(f'Код страны: {match.group(1)}, Код города: {match.group(2)}, Номер: {match.group(3)}')

def logins_re():
    for login in open(0):
        print(bool(re.fullmatch(r'_\d+[a-zA-Z]*_?', login.strip('\n'))))


def two_parts_re():
    for line in open(0):
        line = line.strip('\n')
        match = re.fullmatch(r'(\w+)\1', line)
        if match:
            print(line)


def bee_geek_count():
    bee = 0
    geek = 0
    for line in open(0):
        line = line.strip('\n')
        match1 = re.fullmatch(r'(.*(bee).*){2,}', line)
        match2 = re.fullmatch(r'(.*(\bgeek\b).*)+', line)
        if match1: bee += 1
        if match2: geek += 1
    print(bee)
    print(geek)


def beegeek_rating():
    total = 0
    regex = {
        r'beegeek.*beegeek': 3,
        r'(beegeek).*[^k]': 2,
        r'[^b].*(beegeek)': 2,
        r'[^b].*(beegeek).*[^k]': 1
    }
    for line in open(0):
        line = line.strip('\n')
        for reg, score in regex.items():
            if re.fullmatch(reg, line):
                total += score
    print(total)


def hi_mail():
    regex = [
        r'Здравствуйте',
        r'Доброе утро',
        r'Добрый день',
        r'Добрый вечер'
    ]
    line = input()
    for reg in regex:
        if re.match(reg, line, re.I):
            print(True)
            break
    else:
        print(False)

def sum_bool():
    print(sum(bool(re.search(r'beegeek', line, re.I)) for line in open(0)))