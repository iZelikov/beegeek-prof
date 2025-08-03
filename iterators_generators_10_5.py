from turtledemo.penrose import start


def simple_sequence():
    n = 1
    while True:
        for _ in range(n):
            yield n
        n += 1


def alternating_sequence(count: int = None):
    n = 0
    while n != count:
        n += 1
        yield n * -(-1) ** (n % 2)


def primes(left: int, right: int):
    left = max(left, 2)
    sieve = [1] * (right + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, int(right ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = [0] * len(sieve[i * i::i])
    return (num for num, is_prime in enumerate(sieve) if is_prime and num >= left)


def reverse(sequence):
    for i in range(len(sequence)):
        yield sequence[~i]


from datetime import date


def dates(start: date, count: int = None):
    ordate = start = start.toordinal()
    while ordate - start != count:
        try:
            yield date.fromordinal(ordate)
        except ValueError:
            return
        ordate += 1


def card_deck(suit: str):
    card_nominals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
    card_types = ['пик', 'треф', 'бубен', 'червей']
    card_types.remove(suit)
    n = 0
    while True:
        card_nominal = card_nominals[n % len(card_nominals)]
        card_type = card_types[n // len(card_nominals)]
        n = (n + 1) % (len(card_nominals) * len(card_types))
        yield f'{card_nominal} {card_type}'


def matrix_by_elem(matrix: list[list]):
    yield from sum(matrix, [])

# Неэффективное решение в лоб
# def palindromes():
#     n = 0
#     while True:
#         n+=1
#         if str(n) == str(n)[::-1]:
#             yield n

# Небольшая оптимизация
def palindromes():
    n = 1
    yield from range(1, 10)
    while True:
        n += 1
        for left in range(10 ** (n // 2 - 1), 10 ** (n // 2)):
            s_left = str(left)
            if n % 2:
                for mid in range(10):
                    yield int(s_left + str(mid) + s_left[::-1])
            else:
                yield int(s_left + s_left[::-1])

def flatten(nested_list: list):
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item