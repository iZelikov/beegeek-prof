import re


def normalize_jpeg(filename: str) -> str:
    return re.sub(r'(?P<filename>.+)\.jpe?g$', r'\g<filename>.jpg', filename, flags=re.I)


def normalize_whitespace(string):
    result = re.sub(r'\s{2,}', r' ', string)
    return re.sub(r'\s+$', r'', result)


def forbidden_kw():
    import keyword
    def is_forbidden(match: re.Match) -> str:
        if match[0].lower() in forbidden_set:
            return '<kw>'
        return match[0]

    forbidden_set = set(map(str.lower, keyword.kwlist))
    print(re.sub(r'\w+', repl=is_forbidden, string=input()))


def second_first():
    print(re.sub(r'(\w)(\w)(\w*)', r'\2\1\3', input()))


def unpack():
    def func(s: str) -> str:
        return func(re.sub(r'(\d+)\((\w+)\)', lambda x: int(x[1]) * x[2], s)) if '(' in s else s

    print(func(input()))


def double_word():
    print(re.sub(r'(\b\w+)\W+(\1(\W+))+', r'\1\3', input()))


def no_comments():
    print(re.sub(r'^[ \t]*#.*\n?|[ \t]*#.*$|^\s*"""[^"]*"""\n?', '', open(0).read(), flags=re.M))
