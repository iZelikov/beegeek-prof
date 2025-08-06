from itertools import dropwhile, takewhile, filterfalse, islice, compress, count


def drop_while_negative(iterable):
    yield from dropwhile(lambda x: x < 0, iterable)


def drop_this(iterable, obj):
    yield from dropwhile(lambda x: x == obj, iterable)


def first_true(iterable, predicate):
    return next(filter(predicate, iterable), None)


def take(iterable, n: int):
    yield from islice(iterable, n)

def take_nth(iterable, n: int):
    return next(islice(iterable, n-1, n), None)

def first_largest(iterable, number):
    return next(compress(count(),(x > number for x in iterable)), -1)
