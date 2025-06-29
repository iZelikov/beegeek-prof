def hide_card(raw_card_number: str) -> str:
    card_number = [i for i in raw_card_number if i != ' ']
    return '*' * 12 + ''.join(card_number[12:])


def same_parity(numbers: list) -> list:
    return [i for i in numbers if i % 2 == numbers[0] % 2]


def is_valid(string: str) -> bool:
    return string.isdigit() and len(string) in [4, 5, 6]


def print_given(*args, **kwargs):
    for elem in args:
        print(elem, type(elem))
    for key, value in sorted(kwargs.items()):
        print(key, value, type(value))


def convert(string: str) -> str:
    low = len([c for c in string if c.islower()])
    up = len([c for c in string if c.isupper()])
    return string.lower() if low >= up else string.upper()


def filter_anagrams(word: str, words: list) -> list:
    def get_freq(s: str) -> dict:
        return {c: s.count(c) for c in set(s)}

    return [w for w in words if get_freq(w) == get_freq(word)]


def likes(names: list) -> str:
    match len(names):
        case 0:
            return 'Никто не оценил данную запись'
        case 1:
            return f'{names[0]} оценил(а) данную запись'
        case 2:
            return f'{names[0]} и {names[1]} оценили данную запись'
        case 3:
            return f'{names[0]}, {names[1]} и {names[2]} оценили данную запись'
        case _:
            return f'{names[0]}, {names[1]} и {len(names) - 2} других оценили данную запись'
