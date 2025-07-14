from collections import Counter


def most_common():
    print(Counter(input().lower().split()).most_common(1)[0][0])


def less_common():
    sorted_counter = Counter(input().lower().split()).most_common()[::-1]
    filtered_counter = filter(lambda x: x[1] == sorted_counter[0][1], sorted_counter)
    print(*map(lambda x: x[0], sorted(filtered_counter)), sep=', ')


def find_words():
    sorted_counter = Counter(input().lower().split()).most_common()
    filtered_counter = filter(lambda x: x[1] == sorted_counter[0][1], sorted_counter)
    print(sorted(filtered_counter)[::-1][0][0])


def length_count():
    lengths = Counter(map(len, input().lower().split())).items()
    [print(f'Слов длины {k}: {v}') for k, v in sorted(lengths, key=lambda x: x[1])]


def not_last():
    import sys
    print(Counter({(x := l.split())[0]: int(x[1]) for l in sys.stdin}).most_common()[-2][0])


def modify_data(data: Counter):
    data.min_values = lambda: [x for x in data.items() if x[1] == data.most_common()[-1][1]]
    data.max_values = lambda: [x for x in data.items() if x[1] == data.most_common()[0][1]]


def emails_count():
    import csv
    with open('name_log.csv') as f:
        [print(f'{e}: {c}') for e, c in sorted(Counter(x['email'] for x in csv.DictReader(f)).items())]


def scrabble(symbols: str, word: str) -> bool:
    return Counter(symbols.lower()) >= Counter(word.lower())


def print_bar_chart(data: str | list, mark: str):
    max_length = len(max(data, key=len))
    [print(f'{s:{max_length}} |{mark * count}') for s, count in Counter(data).most_common()]


def happy_farmer():
    import csv
    import json
    year_result = Counter()
    for i in range(1, 5):
        with open(f'quarter{i}.csv', encoding='utf8') as file:
            year_result += Counter({x[0]: sum(map(int, x[1:])) for x in list(csv.reader(file))[1:]})
    with open('prices.json', encoding='utf8') as jsn:
        prices = json.load(jsn)
        print(sum(map(lambda x: prices[x[0]] * x[1], year_result.items())))


def books_seller():
    books = Counter(input().split())
    profit = 0
    for _ in range(int(input())):
        book, money = input().split()
        if books[book]:
            books -= Counter([book])
            profit += int(money)
    print(profit)


books_seller()
