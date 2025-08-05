def alive_swedish():
    from collections import namedtuple
    Person = namedtuple('Person', ['name', 'nationality', 'sex', 'birth', 'death'])
    persons = [Person('E. M. Ashe', 'American', 'male', 1867, 1941),
               Person('Goran Aslin', 'Swedish', 'male', 1980, 0),
               Person('Erik Gunnar Asplund', 'Swedish', 'male', 1885, 1940),
               Person('Genevieve Asse', 'French', 'female', 1949, 0),
               Person('Irene Adler', 'Swedish', 'female', 2005, 0),
               Person('Sergio Asti', 'Italian', 'male', 1926, 0),
               Person('Olof Backman', 'Swedish', 'male', 1999, 0),
               Person('Alyson Hannigan', 'Swedish', 'female', 1940, 1987),
               Person('Dana Atchley', 'American', 'female', 1941, 2000),
               Person('Monika Andersson', 'Swedish', 'female', 1957, 0),
               Person('Shura_Stone', 'Russian', 'male', 2000, 0),
               Person('Jon Bale', 'Swedish', 'male', 2000, 0)]

    def alive(people: list[Person]):
        return (man for man in people if not man.death)

    def swedish(people: list[Person]):
        return (man for man in people if man.nationality == 'Swedish')

    def men(people: list[Person]):
        return (man for man in people if man.sex == 'male')

    def youngest(people: list[Person]):
        return max(people, key=lambda man: man.birth)

    print(youngest(alive(men(swedish(persons)))).name)


def parse_ranges(ranges: str):
    def get_range_str():
        result = []
        for c in ranges:
            if c == ',':
                yield ''.join(result)
                result = []
            else:
                result.append(c)
        yield ''.join(result)

    ranges_list = get_range_str()
    ranges_borders = (r.split('-') for r in ranges_list)
    range_ranges = (range(int(a), int(b) + 1) for a, b in ranges_borders)
    for item in range_ranges:
        yield from item


def filter_names(names: list[str], ignore_char: str, max_names: int):
    f_ignored = (name for name in names if name[0].lower() != ignore_char.lower())
    f_alpha = (name for name in f_ignored if name.isalpha())
    f_limit = (name for i, name in enumerate(f_alpha) if i < max_names)
    yield from f_limit


def investments():
    with open('data.csv', encoding='utf-8') as file:
        headers = next(file).strip().split(',')
        invests = (row.strip().split(',') for row in file)
        filter_a = (int(m) for c, m, r in invests if r == 'a')
        print(sum(filter_a))


def years_days(year):
    from datetime import date
    dates = range(date(year, 1, 1).toordinal(), date(year + 1, 1, 1).toordinal())
    return (date.fromordinal(d) for d in dates)


def nonempty_lines(file):
    with open(file, encoding='utf-8') as f:
        yield from ('...' if len(line) > 26 else line.strip() for line in f if line.strip())


def txt_to_dict():
    with open('planets.txt', encoding='utf-8') as file:
        while True:
            d = {}
            for bee in "geek":
                d.update([tuple(next(file).strip().split(' = '))])
            yield d
            try:
                next(file)
            except:
                break


def unique(iterable):
    used = set()
    for i in iterable:
        if i not in used:
            used.add(i)
            yield i


def stop_on(iterable, obj):
    yield from iter(iter(iterable).__next__, obj)


def with_previous(iterable):
    prev = None
    for i in iterable:
        yield i, prev
        prev = i

def pairwise(iterable):
    it = iter(iterable)
    nxt = next(it, None)
    while nxt is not None:
        nxt, current = next(it, None), nxt
        yield current, nxt

def around(iterable):
    it = iter(iterable)
    cur = None
    nxt = next(it, None)
    while nxt is not None:
        prv, cur, nxt = cur, nxt, next(it, None)
        yield prv, cur, nxt