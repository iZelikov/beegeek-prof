import sys


def numbers_sum(elems):
    '''Принимает список и возвращает сумму его чисел (int, float),
игнорируя нечисловые объекты. 0 - если в списке чисел нет.'''
    return sum(map(lambda x: x if isinstance(x, (int, float)) else 0, elems), 0)


# Закомментирован, чтобы не ломать стандартный принт
# def print(*args, sep=" ", end='\n'):
#     translate = lambda x: x.upper() if isinstance(x, str) else str(x)
#     sys.stdout.write(sep.upper().join(map(translate, args)))
#     sys.stdout.write(end.upper())

def polynom(x: int) -> int:
    result = x ** 2 + 1
    polynom.__dict__.setdefault('values', set()).add(result)
    return result


def remove_marks(text: str, marks: str) -> str:
    remove_marks.__dict__['count'] = remove_marks.__dict__.get('count', 0) + 1
    for mark in marks:
        text = text.replace(mark,'')
    return text
