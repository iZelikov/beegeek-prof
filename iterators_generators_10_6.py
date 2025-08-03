def cubes_of_odds(iterable):
    return (i ** 3 for i in iterable if i % 2)


def is_prime(number: int) -> bool:
    return all(number % i for i in range(2, int(number ** 0.5) + 1)) if number - 1 else False


def count_iterable(iterable):
    return sum(1 for _ in iterable)

def all_together(*args):
    return (elem for iterable in args for elem in iterable)

def interleave(*args):
    return (seq[i] for i in range(len(args[0])) for seq in args)