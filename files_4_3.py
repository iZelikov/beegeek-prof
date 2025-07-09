import json


def format_countries():
    countries = {'Monaco': 'Monaco', 'Iceland': 'Reykjavik', 'Kenya': 'Nairobi', 'Kazakhstan': 'Nur-Sultan',
                 'Mali': 'Bamako', 'Colombia': 'Bogota', 'Finland': 'Helsinki', 'Costa Rica': 'San Jose',
                 'Cuba': 'Havana', 'France': 'Paris', 'Gabon': 'Libreville', 'Liberia': 'Monrovia',
                 'Angola': 'Luanda', 'India': 'New Delhi', 'Canada': 'Ottawa', 'Australia': 'Canberra'}
    print(json.dumps(countries, sort_keys=True, separators=(',', ' - '), indent=3))


def skip_keys():
    words = {
        frozenset(["tap", "telephone"]): ("tæp", "telifəun"),
        "travel": "trævl",
        ("hello", "world"): ("həˈləʊ", "wɜːld"),
        "moonlight": "muːn.laɪt",
        "sunshine": "ˈsʌn.ʃaɪn",
        ("why", "is", "so", "difficult"): ("waɪ", "ɪz", "səʊ", "ˈdɪfɪkəlt"),
        "adventure": "ədˈventʃər",
        "beautiful": "ˈbjuːtɪfl",
        frozenset(["spoon", "block"]): ("spu:n", "blɔk"),
        "bicycle": "baisikl",
        ("pilot", "fly"): ("pailət", "flai")
    }
    data_json = json.dumps(words, skipkeys=True)


def dum_clubs():
    club1 = {"name": "FC Byern Munchen", "country": "Germany", "founded": 1900,
             "trainer": "Julian Nagelsmann", "goalkeeper": "M. Neuer", "league_position": 1}
    club2 = {"name": "FC Barcelona", "country": "Spain", "founded": 1899,
             "trainer": "Xavier Creus", "goalkeeper": "M. Ter Stegen", "league_position": 7}
    club3 = {"name": "FC Manchester United", "country": "England", "founded": 1878,
             "trainer": "Michael Carrick", "goalkeeper": "D. De Gea", "league_position": 8}
    with open('data.json', 'w', encoding='utf8') as file:
        json.dump([club1, club2, club3], file, indent=3)


def ensure_utf():
    specs = {
        'Модель': 'AMD Ryzen 5 5600G',
        'Год релиза': 2021,
        'Сокет': 'AM4',
        'Техпроцесс': '7 нм',
        'Ядро': 'Cezanne',
        'Объем кэша L2': '3 МБ',
        'Объем кэша L3': '16 МБ',
        'Базовая частота': '3900 МГц'
    }
    specs_json = json.dumps(specs, ensure_ascii=False, indent=3)
    print(specs_json)


def is_correct_json(string):
    from json import JSONDecodeError
    try:
        json.loads(string)
        return True
    except JSONDecodeError:
        return False


def json_elements():
    import sys
    obj = json.load(sys.stdin)
    for k, v in obj.items():
        if isinstance(v, list):
            print(f"{k}: {", ".join(map(str, v))}")
        else:
            print(f"{k}: {v}")


def different_types():
    with open('data.json', encoding='utf8') as file_in:
        result = []
        for item in json.load(file_in):
            if isinstance(item, str):
                result.append(item + '!')
            elif isinstance(item, bool):
                result.append(not item)
            elif isinstance(item, int):
                result.append(item + 1)
            elif isinstance(item, list):
                result.append(item * 2)
            elif isinstance(item, dict):
                item['newkey'] = None
                result.append(item)
    with open('updated_data.json', 'w', encoding='utf8') as file_out:
        json.dump(result, file_out)


def merge_objects():
    with open('data1.json', encoding='utf8') as f1, open('data2.json', encoding='utf8') as f2:
        result, data2 = json.load(f1), json.load(f2)
        result.update(data2)
    with open('data_merge.json', 'w', encoding='utf8') as file_out:
        json.dump(result, file_out)


def empty_keys():
    with open('people.json', encoding='utf8') as f1:
        data = json.load(f1)
        keys = set()
        for item in data:
            keys.update(item.keys())
        empty_dict = dict.fromkeys(keys, None)
        result = [empty_dict | item for item in data]
    with open('updated_people.json', 'w', encoding='utf8') as file_out:
        json.dump(result, file_out)


def python_religion():
    with open('countries.json', encoding='utf8') as f1:
        data = json.load(f1)
        result = {}
        for item in data:
            result.setdefault(item['religion'], []).append(item['country'])
    with open('religion.json', 'w', encoding='utf8') as file_out:
        json.dump(result, file_out)


def parks_addresses():
    import csv

    with open('playgrounds.csv', encoding='utf8') as f1:
        table = csv.DictReader(f1, delimiter=';')
        result = {}
        for row in table:
            result.setdefault(row['AdmArea'], {}).setdefault(row['District'], []).append(row['Address'])

    with open('addresses.json', 'w', encoding='utf8') as file_out:
        json.dump(result, file_out, ensure_ascii=False)


def students_course():
    import csv
    with open('students.json', encoding='utf8') as file_in:
        table = json.load(file_in)
        result = [dict(name=s['name'], phone=s['phone']) for s in table if s['age'] >= 18 and s['progress'] >= 75]
    with open('data.csv', 'w', encoding='utf8', newline='') as file_out:
        writer = csv.DictWriter(file_out, fieldnames=['name', 'phone'])
        writer.writeheader()
        writer.writerows(sorted(result, key=lambda x: x['name']))


def best_pools():
    from datetime import datetime, timedelta
    def filter_time(d):
        format_t = '%H:%M'
        t = d['WorkingHoursSummer'].get('Понедельник')
        start, end = t.split('-')
        return (datetime.strptime(start, format_t) <= datetime.strptime('10:00', format_t)
                and datetime.strptime(end, format_t) >= datetime.strptime('12:00', format_t))

    with open('pools.json', encoding='utf8') as file_in:
        table = json.load(file_in)
        t_filtered = list(filter(filter_time, table))
        l_max = max(t_filtered,
                    key=lambda x: (x['DimensionsSummer'].get('Length', 0), x['DimensionsSummer'].get('Width', 0)))
        print(f'{l_max['DimensionsSummer'].get('Length', 0)}x{l_max['DimensionsSummer'].get('Width', 0)}')
        print(l_max['Address'])


def best_scores():
    import csv
    from datetime import datetime, timedelta
    with open('exam_results.csv', encoding='utf8') as file_in:
        table = sorted(list(csv.DictReader(file_in)),
                       key=lambda x: (x['email'], -int(x['score']),
                                      -datetime.fromisoformat(x['date_and_time']).toordinal()))
        processed = set()
        result = []
        for row in table:
            if not row['email'] in processed:
                row['best_score'] = int(row.pop('score'))
                result.append(row)
                processed.add(row['email'])
    with open('best_scores.json', 'w', encoding='utf8') as file_out:
        json.dump(result, file_out, ensure_ascii=False)

def food_services():
    with open('food_services.json', encoding='utf8') as file_in:
        table = json.load(file_in)
        districts = {}
        companies = {}
        for row in table:
            districts[row["District"]] = districts.get(row["District"], 0) + 1
            companies[row["OperatingCompany"]] = companies.get(row["OperatingCompany"], 0) + bool(
                row["OperatingCompany"])
        print(*max(districts.items(), key=lambda x: x[1]), sep=': ')
        print(*max(companies.items(), key=lambda x: x[1]), sep=': ')

def food_services_seats():
    with open('food_services.json', encoding='utf8') as file_in:
        table = json.load(file_in)
        types = {}
        for row in table:
            types.setdefault(row['TypeObject'], []).append((row['SeatsCount'], row['Name']))

        for food_type, food_list in sorted(types.items()):
            print(f'{food_type}: {max(food_list)[1]}, {max(food_list)[0]}')