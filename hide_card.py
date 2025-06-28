def hide_card(raw_card_number: str) -> str:
    card_number = [i for i in raw_card_number if i != ' ']
    return '*' * 12 + ''.join(card_number[12:])


card = '905 678123 45612 56'
print(hide_card(card))
