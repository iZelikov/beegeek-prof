
infinite_love = iter(lambda: "i love beegeek!", None)

def is_iterable(obj):
    try:
        iter(obj)
        return True
    except:
        return False

def is_iterator(obj):
    return '__next__' in dir(obj)

def random_numbers(left, right):
    return iter(lambda: __import__('random').randint(left, right), None)