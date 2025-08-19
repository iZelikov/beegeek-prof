import re


def split_semicolon():
    print(*re.split(r'\s*[.,;]\s*', input()))


def split_logic():
    print(*re.split(r'\s*[&|]\s*|\s*and\s*|\s*or\s*', input(), flags=re.I), sep=', ')


def multiple_split(string: str, delimiters):
    return re.split('|'.join(re.escape(d) for d in delimiters), string)


def sum_digits():
    start, end = map(int, input().split())
    pattern = re.compile(r'\d+')
    print(sum(map(int, pattern.findall(input(), pos=start, endpos=end))))