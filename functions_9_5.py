from datetime import date


def power(degree: int):
    return lambda x: x ** degree


def generator_square_polynom(a: float, b: float, c: float):
    return lambda x: a * x ** 2 + b * x + c


def sourcetemplate(url: str):
    def inner(**kwargs):
        return url + '?' + '&'.join(f'{k}={v}' for k, v in sorted(kwargs.items())) if kwargs else url

    return inner


def date_formatter(country_code: str):
    import datetime
    formats = {
        'ru': '%d.%m.%Y',
        'us': '%m-%d-%Y',
        'ca': '%Y-%m-%d',
        'br': '%d/%m/%Y',
        'fr': '%d.%m.%Y',
        'pt': '%d-%m-%Y'
    }

    def inner(d: datetime.date):
        return d.strftime(formats[country_code])

    return inner


def sort_priority(values, group):
    values.sort(key=lambda x: (x not in group, x))
