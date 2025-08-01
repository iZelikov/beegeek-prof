def filterfalse(predicate, iterable):
    return filter(lambda x: not x if predicate is None else not predicate(x), iterable)


def transpose(matrix: list[list]):
    return list(map(list, zip(*matrix)))


# закомментировано из-за конфликта имён
# def get_min_max(data: list):
#     return tuple(map(lambda f: data.index(f(data)), (min, max))) if data else None


def starmap(func, iterable):
    return map(lambda x: func(*x), iterable)


def get_min_max(iterable):
    it = iter(iterable)
    try:
        min_i = max_i = next(it)
    except:
        return None
    for i in it:
        min_i = i if min_i > i else min_i
        max_i = i if max_i < i else max_i
    return min_i, max_i
