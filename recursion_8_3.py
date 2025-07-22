def count_digits(n: int) -> int:
    return 1 if n < 10 else count_digits(n // 10) + 1


def sum_digits(n: int) -> int:
    return n % 10 + sum_digits(n // 10) if n > 9 else n


def number_of_frogs(year: int, frogs: int = 77) -> int:
    if not year - 1:
        return frogs
    return number_of_frogs(year - 1, 3 * (frogs - 30))


def range_sum(numbers: list, start: int, end: int) -> int:
    if start == end:
        return numbers[end]
    return numbers[start] + range_sum(numbers, start + 1, end)


def get_pow(a: int, n: int) -> int:
    if not n:
        return 1
    return a * get_pow(a, n - 1)


def get_fast_pow(a: int, n: int) -> int:
    import sys
    sys.set_int_max_str_digits(1000000)
    if not n:
        return 1
    if n % 2:
        return a * get_fast_pow(a, n - 1)
    else:
        return get_fast_pow(a * a, n // 2)


def recursive_sum(a: int, b: int) -> int:
    return recursive_sum(a + 1, b - 1) if b else a


def is_power(number: int) -> bool:
    if number == 1:
        return True
    elif number % 2:
        return False
    return is_power(number // 2)


def tribonacci(n) -> int:
    cache = {1: 1, 2: 1, 3: 1}

    def rec(n):
        result = cache.get(n)
        if result is None:
            result = rec(n - 3) + rec(n - 2) + rec(n - 1)
            cache[n] = result
        return result

    return rec(n)


def is_palindrome(string: str) -> bool:
    if not string:
        return True
    if string[0] == string[-1]:
        return is_palindrome(string[1:-1])
    return False


def to_binary(n: int) -> str:
    return str(n) if n < 2 else to_binary(n // 2) + str(n % 2)


def no_loops(start, diff=5, n=None, reverse=False):
    if n is None:
        n = start
    elif n <= 0:
        reverse = True
    elif n == start:
        print(n)
        return
    print(n)
    no_loops(start, n = n - (diff, -diff)[reverse], reverse=reverse)


no_loops(int(input()))
