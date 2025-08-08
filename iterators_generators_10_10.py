import operator
from itertools import chain, tee, pairwise, starmap, zip_longest, repeat


def sum_of_digits(iterable):
    return sum(map(int, chain(*map(str, iterable))))


def is_rising(iterable):
    return all(map(lambda x: x[0] < x[1], pairwise(iterable)))


def max_pair(iterable):
    return max(starmap(operator.add, pairwise(iterable)))


def ncycles(iterable, times: int):
    yield from chain.from_iterable(tee(iterable, times))


def grouper(iterable, n: int):
    return zip_longest(*repeat(iter(iterable), n))
