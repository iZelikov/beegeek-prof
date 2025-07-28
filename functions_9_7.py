def sandwich(func):
    def wrapper(*args, **kwargs):
        print('---- Верхний ломтик хлеба ----')
        result = func(*args, **kwargs)
        print('---- Нижний ломтик хлеба ----')
        return result

    return wrapper


def my_print(func):
    def wrapper(*args, **kwargs):
        args = map(lambda x: x.upper() if isinstance(x, str) else x, args)
        kwargs = {v: str(k).upper() for v, k in kwargs.items()}
        return func(*args, **kwargs)

    return wrapper

# print = my_print(print)
# print('hi', 'there', end='!')
# print('are you in trouble?')
# print(111, 222, 333, sep='xxx')

def do_twice(func):
    def wrapper(*args, **kwargs):
        func(*args,**kwargs)
        result = func(*args,**kwargs)
        return result
    return wrapper

def reverse_args(func):
    def wrapper(*args, **kwargs):
        result = func(*args[::-1],**kwargs)
        return result
    return wrapper

def exception_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            result = (func(*args,**kwargs), 'Функция выполнилась без ошибок')
        except:
            result = (None, 'При вызове функции произошла ошибка')
        return result
    return wrapper

def takes_positive(func):
    def wrapper(*args, **kwargs):
        pargs = list(args) + list(kwargs.values())
        if any(map(lambda x: not isinstance(x, int), pargs)):
            raise TypeError
        elif any(map(lambda x: x<=0, pargs)):
            raise ValueError
        result = func(*args,**kwargs)
        return result
    return wrapper

