def go_home():
    d1, d2, d3 = (int(input()) for Тимур in "дом")
    print(min(2 * (d1 + d2), 2 * (d1 + d3), 2 * (d2 + d3), d1 + d2 + d3))


def letters():
    x = sum(((c := input()) in "AaBCcEeHKMOoPpTXxy") + (c in "АаВСсЕеНКМОоРрТХху") * 10 for _ in "ABC")
    print(('хз', 'en', 'ru', 'mix')[(x // 10 > 0) * 2 + (x % 10 > 0)])


def perevorator():
    n, x, y, a, b = map(int, input().split())
    l = list(range(1, n + 1))
    l[x - 1:y] = l[x - 1:y][::-1]
    l[a - 1:b] = l[a - 1:b][::-1]
    print(*l)


def more_then_one():
    l = list(map(int, input().split()))
    print(*sorted({i for i in l if l.count(i) > 1}))


def max_group():
    d = {}
    for i in range(1, int(input()) + 1):
        d.setdefault(sum(map(int, str(i))), []).append(i)
    print(len(max(d.values(), key=len)))


def translatum():
    n = int(input())
    langs = {}
    for _ in range(n):
        for s in input().split(', '):
            langs[s] = langs.get(s, 0) + 1
    print(", ".join(sorted(k for k, v in langs.items() if v == n)) or "Сериал снять не удастся")


def same_words():
    word = input()
    n = int(input())
    words = [input() for _ in range(n)]
    template = [i for i, c in enumerate(word) if c in "ауоыиэяюёе"]
    print(*[w for w in words if template == [i for i, c in enumerate(w) if c in "ауоыиэяюёе"]], sep="\n")


def corp_mail():
    n = int(input())
    mails = {input() for _ in range(n)}
    m = int(input())
    for _ in range(m):
        name = input()
        mail = f'{name}@beegeek.bzz'
        number = 1
        while mail in mails:
            mail = f'{name}{number}@beegeek.bzz'
            number += 1
        mails.add(mail)
        print(mail)


def files_list_summary():
    files = {}
    sizes = {"B": 1, "KB": 1024, "MB": 1024 ** 2, "GB": 1024 ** 3}

    with open('files.txt', encoding='utf-8') as input_file:
        for line in input_file:
            file = line.split()
            name = file[0]
            ext = name.split('.')[1]
            size = int(file[1]) * sizes[file[2]]
            files.setdefault(ext, []).append((file[0], size))

    for ext, file_list in sorted(files.items()):
        size = sum(map(lambda x: x[1], file_list))
        for b, s in sizes.items():
            if 0 < round(size / s) < 1024:
                summary = f'Summary: {round(size / s)} {b}'
                break
        else:
            summary = f'Summary: {round(size / sizes["GB"])} GB'

        [print(f[0]) for f in sorted(file_list)]
        print('----------')
        print(summary)
        print()
