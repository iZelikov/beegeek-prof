class Repeater:
    def __init__(self, obj):
        self.obj = obj

    def __iter__(self):
        return self

    def __next__(self):
        return self.obj


class BoundedRepeater:
    def __init__(self, obj, times):
        self.obj = obj
        self.times = times

    def __iter__(self):
        return self

    def __next__(self):
        if not self.times:
            raise StopIteration
        else:
            self.times -= 1
            return self.obj


class Square:
    def __init__(self, n):
        self.n = n
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == self.n:
            raise StopIteration
        else:
            self.counter += 1
            return self.counter ** 2


class Fibonacci:
    def __init__(self):
        self.prev = None
        self.prev_prev = None

    def __iter__(self):
        return self

    def __next__(self):
        if not self.prev or not self.prev_prev:
            self.prev_prev, self.prev = self.prev, 1
            return 1
        else:
            result = self.prev + self.prev_prev
            self.prev_prev, self.prev = self.prev, result
            return result


class PowerOf:
    def __init__(self, number):
        self.number = number
        self.power = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.power += 1
        return self.number ** self.power


class DictItemsIterator:
    def __init__(self, data: dict):
        self.data = data
        self.i_data = iter(data)

    def __iter__(self):
        return self

    def __next__(self):
        key = next(self.i_data)
        value = self.data[key]
        return key, value


class CardDeck:
    def __init__(self):
        self._card_nominals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
        self._card_types = ['пик', 'треф', 'бубен', 'червей']
        self.deck = range(len(self._card_nominals) * len(self._card_types))
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == len(self.deck):
            raise StopIteration
        card_nominal = self._card_nominals[self.current % len(self._card_nominals)]
        card_type = self._card_types[self.current // len(self._card_nominals)]
        self.current += 1
        return f'{card_nominal} {card_type}'


class Cycle:
    def __init__(self, iterable):
        self.iterable = iterable
        self.l = len(iterable)
        self.counter = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.counter = (self.counter + 1) % self.l
        return self.iterable[self.counter]


class RandomNumbers:
    def __init__(self, left: int, right: int, n: int):
        self.rand = __import__('random')
        self.left = left
        self.right = right
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if not self.n:
            raise StopIteration
        self.n -= 1
        return self.rand.randint(self.left, self.right)


class Alphabet:
    def __init__(self, language):
        self.lang = language
        self.index = -1
        self.alph = {
            "ru": [chr(c) for c in range(ord('а'), ord('я') + 1)],
            "en": [chr(c) for c in range(ord('a'), ord('z') + 1)]
        }

    def __iter__(self):
        return self

    def __next__(self):
        alph = self.alph.get(self.lang)
        self.index = (self.index + 1) % len(alph)
        return alph[self.index]


class Xrange:
    def __init__(self, start: int | float, end: int | float, step: int | float = 1):
        self.start = start - step
        self.end = end
        self.step = step
    def __iter__(self):
        return self
    def __next__(self):
        self.start += self.step
        if self.step < 0 and self.start <= self.end:
            raise StopIteration
        elif self.step >= 0 and self.start >= self.end:
            raise StopIteration
        return self.start
