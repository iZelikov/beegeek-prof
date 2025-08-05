from itertools import count, accumulate, cycle


def tabulate(func):
    yield from map(func, count(1, 1))


def factorials(n: int):
    from itertools import accumulate
    import operator
    yield from accumulate(range(1, n + 1), operator.mul)


def alnum_sequence():
    for i in cycle(enumerate((chr(x) for x in range(ord("A"), ord("Z") + 1)), 1)):
        yield from i


def roundrobin(*args):
    cnt = len(args)
    for i in cycle(map(iter, args)):
        try:
            yield next(i)
            cnt = len(args)
        except StopIteration:
            if not cnt:
                break
            cnt -=1

