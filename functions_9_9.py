def part_email():
    from functools import partial
    def send_email(name, email_address, text):
        pass

    to_Timur = partial(send_email, "Тимур", 'timyrik20@beegeek.ru')
    send_an_invitation = partial(send_email,
                                 text='Школа BEEGEEK приглашает Вас на новый курс по программированию на языке Python. тутут....')


def dima():
    import sys
    from functools import cache
    @cache
    def dima_sort(word: str):
        return ''.join(sorted(word))

    for w in sys.stdin.readlines():
        print(dima_sort(w.rstrip()))


from functools import cache
@cache
def ways(n: int) -> int:
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        return ways(n-1) + ways(n-3) + ways(n-4)
