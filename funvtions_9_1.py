def latin():
    [print(chr(i)) for i in range(ord('a'), ord('z') + 1)]


def convert(number: int):
    return f'{number:b}', f'{number:o}', f'{number:X}'


def worst_film():
    films = {'Spider-Man: No Way Home': {'imdb': 8.8, 'kinopoisk': 8.3},
             'Don"t Look Up': {'imdb': 7.3, 'kinopoisk': 7.6},
             'Encanto': {'imdb': 7.3, 'kinopoisk': 7.4},
             'The Witcher': {'imdb': 8.2, 'kinopoisk': 7.3},
             'Ghostbusters: Afterlife': {'imdb': 7.3, 'kinopoisk': 8},
             'Harry Potter 20th Anniversary: Return to Hogwarts': {'imdb': 8.1, 'kinopoisk': 8.2},
             'Shingeki no Kyojin': {'imdb': 9.0, 'kinopoisk': 8.3},
             'The Matrix': {'imdb': 8.7, 'kinopoisk': 8.5},
             'The Dark Knight': {'imdb': 9.0, 'kinopoisk': 8.5},
             'The Shawshank Redemption': {'imdb': 9.3, 'kinopoisk': 9.1},
             'Avengers: Endgame': {'imdb': 8.4, 'kinopoisk': 7.7}}

    print(min(films, key=lambda x: sum(films[x].values())))


def non_negative_even(numbers: list):
    return all(map(lambda x: x >= 0 and not x % 2, numbers))


def is_greater(lists: list, number: int):
    return any(sum(x) > number for x in lists)


def custom_isinstance(objects, typeinfo):
    return len(list(filter(lambda x: isinstance(x, typeinfo), objects)))


def max_index():
    numbers = [-7724, 5023, 3197, -102, -4129, -880, 5857, -2866, -8913, 1195, 9809, 5347, -8071, 903, 3030, -4347,
               -3354, 1024, 8670, 4210, -5228, 8900, 4823, -2002, 4900, 9520, -3658, 1104, -9554, 3064, 9632, -8701,
               3384, 4370, 2034, 7822, -9694, 3347, 7440, -8459, 3238, -5193, -3381, 5281, 9022, 5559, 7593, -6540,
               -6204, -2483, 8729, 5810, -8254, -9846, -1801, 4882, 3838, -3140, 7609, -3325, 6026, 2994, -1677, 1266,
               -1893, -4408, -5722, -2841, 9812, 5837, -7474, 4624, -664, 6998, 7888, -971, 8810, 3812, -5396, 2593,
               512, -4634, 9735, -3062, 9031, -9300, 3657, 6332, 7552, 8125, -725, 4392, 1727, 8194, -2828, -4314,
               -8967, -7912, -1363, -5957]

    print(numbers.index(max(numbers)))


def my_pow(number):
    return sum(int(x) ** i for i, x in enumerate(str(number), 1))

def films_profit():
    names = ['Moana', 'Cars', 'Zootopia', 'Ratatouille', 'Coco', 'Inside Out', 'Finding Nemo', 'Frozen']
    budgets = [150000000, 120000000, 150000000, 150000000, 180000000, 175000000, 94000000, 150000000]
    box_offices = [643331111, 462216280, 1023784195, 620702951, 807082196, 857611174, 940335536, 1280802282]

    [print(f'{name}: {box - bud}$') for name, bud, box in sorted(zip(names, budgets, box_offices))]

def zip_longest(*args, fill=None):
    result = []
    for i in range(max(map(len,args))):
        t = []
        for item in args:
            t.append(item[i] if i < len(item) else fill)
        result.append(tuple(t))
    return result