def square(func):
    import functools
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) ** 2

    return wrapper


def returns_string(func):
    import functools
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result
        else:
            raise TypeError

    return wrapper


def trace(func):
    import functools
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'TRACE: вызов {func.__name__}() с аргументами: {args}, {kwargs}')
        result = func(*args, **kwargs)
        print(f"TRACE: возвращаемое значение {func.__name__}(): {repr(result)}")
        return result

    return wrapper


def prefix(string: str, to_the_end: bool = False):
    def decorator(func):
        import functools
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return "".join((string, func(*args, **kwargs))[::(-1) ** to_the_end])

        return wrapper

    return decorator


def make_html(tag: str):
    def decorator(func):
        import functools
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return f'<{tag}>{func(*args, **kwargs)}</{tag}>'

        return wrapper

    return decorator


def repeat(times=1):
    def decorator(func):
        import functools
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times - 1):
                func(*args, **kwargs)
            return func(*args, **kwargs)

        return wrapper

    return decorator


def strip_range(start: int, end: int, char: str = '.'):
    def decorator(func):
        import functools
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result[:start] + char*(min(end, len(result))-start) + result[end:]
        return wrapper
    return decorator


def returns(datatype):
    def decorator(func):
        import functools
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result,datatype):
                return result
            else:
                raise TypeError
        return wrapper
    return decorator

def takes(*datatypes):
    def decorator(func):
        import functools
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            args = args + tuple(kwargs.values())
            for arg in args:
                if not isinstance(arg, datatypes):
                    raise TypeError
            return result
        return wrapper
    return decorator

def add_attrs(**d_kwargs):
    def decorator(func):
        import functools
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        wrapper.__dict__.update(d_kwargs)
        return wrapper
    return decorator

def ignore_exception(*ex_types):
    def decorator(func):
        import functools
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ex_types as e:
                if isinstance(e, ex_types):
                    print(f'Исключение {type(e).__name__} обработано')
        return wrapper
    return decorator

class MaxRetriesException(Exception):
    pass

def retry(times):
    def decorator(func):
        import functools
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                try:
                    return func(*args, **kwargs)
                except:
                    pass
            raise MaxRetriesException
        return wrapper
    return decorator