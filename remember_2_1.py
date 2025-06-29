def hide_card(raw_card_number: str) -> str:
    card_number = [i for i in raw_card_number if i != ' ']
    return '*' * 12 + ''.join(card_number[12:])


def same_parity(numbers: list) -> list:
    return [i for i in numbers if i % 2 == numbers[0] % 2]


def is_valid(string: str) -> bool:
    return string.isdigit() and len(string) in [4, 5, 6]
