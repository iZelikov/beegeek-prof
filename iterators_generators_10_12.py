from itertools import permutations, combinations, combinations_with_replacement, product, chain


def uniq_permutations():
    [print("".join(x)) for x in sorted(set(permutations(input())))]


def coins():
    wallet = [100, 100, 50, 50, 50, 50, 20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
    print(sum(len(set(x for x in (combinations(wallet, n)) if sum(x) == 100)) for n in range(1, len(wallet))))


def coins_with_replacement():
    wallet = [100, 50, 20, 10, 5]
    print(sum(len(set(x for x in (combinations_with_replacement(wallet, n)) if sum(x) == 100)) for n in range(1, 21)))


def backpack_task_brute_force():
    from collections import namedtuple
    Item = namedtuple('Item', ['name', 'mass', 'price'])
    items = [Item('Обручальное кольцо', 7, 49_000),
             Item('Мобильный телефон', 200, 110_000),
             Item('Ноутбук', 2000, 150_000),
             Item('Ручка Паркер', 20, 37_000),
             Item('Статуэтка Оскар', 4000, 28_000),
             Item('Наушники', 150, 11_000),
             Item('Гитара', 1500, 32_000),
             Item('Золотая монета', 8, 140_000),
             Item('Фотоаппарат', 720, 79_000),
             Item('Лимитированные кроссовки', 300, 80_000)]
    limit = int(input())
    result = []
    for n in range(1, len(items) + 1):
        backpack = [(sum(map(lambda x: x.price, i)), i) for i in combinations(items, n) if
                    sum(map(lambda x: x.mass, i)) <= limit]
        if backpack:
            result.append(max(backpack))
    if result:
        print(*sorted(map(lambda x: x.name, max(result)[1])), sep='\n')
    else:
        print('Рюкзак собрать не удастся')


def password_gen():
    yield from map(lambda x: str(x).zfill(3), range(1000))


def gen_numbers():
    n, m = int(input()), int(input())
    seq = range(n) if n <= 10 else chain(range(10), "ABCDEF"[:(n - 10)])
    print(*map("".join, product(map(str, seq), repeat=m)))


gen_numbers()
