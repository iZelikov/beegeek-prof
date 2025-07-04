def calculate_it(func,*args):
    from time import perf_counter
    start = perf_counter()
    result = func(*args)
    end = perf_counter()
    return result, end-start

def get_the_fastest_func(funcs, arg):
    return min((calculate_it(f, arg)[1], f) for f in funcs)[1]


def for_and_append(iterable):  # с использованием цикла for и метода append()
    result = []
    for elem in iterable:
        result.append(elem)
    return result


def list_comprehension(iterable):  # с использованием списочного выражения
    return [elem for elem in iterable]


def list_function(iterable):  # с использованием встроенной функции list()
    return list(iterable)



print(calculate_it(for_and_append, range(100_000))[1])
print(calculate_it(list_comprehension,range(100_000))[1])
print(calculate_it(list_function,range(100_000))[1])

