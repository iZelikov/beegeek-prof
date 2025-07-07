import csv


def wrong_reader():
    with open('grades.csv', encoding='utf-8') as csv_file:
        # считываем содержимое файла
        # text = csv_file.read()
        # создаем reader объект и указываем в качестве разделителя символ ;
        rows = csv.reader(csv_file, delimiter=';')
        # выводим каждую строку
        for row in rows:
            print(row)


def dick_write():
    with open('writing_test.csv', 'w', encoding='utf-8', newline='') as csv_file:
        # создаем writer объект и указываем названия столбцов
        writer = csv.DictWriter(csv_file, fieldnames=['first_col', 'second_col'])
        # записываем первую строку с названиями столбцов
        writer.writeheader()
        # записываем строку с данными
        writer.writerow({'first_col': 'value1', 'second_col': 'value2'})


def discounts():
    with open('sales.csv', encoding='utf-8') as file:
        rows = csv.DictReader(file, delimiter=';')
        print(*map(lambda x: x['name'], filter(lambda r: int(r['old_price']) > int(r['new_price']), rows)), sep="\n")


def avg_salary():
    with open('salary_data.csv', encoding='utf-8') as file:
        rows = csv.DictReader(file, delimiter=';')
        companies = {}
        for row in rows:
            companies.setdefault(row['company_name'], []).append(int(row['salary']))
    print(*sorted(companies, key=lambda x: sum(companies[x]) / len(companies[x])), sep='\n')


def deniro_csv():
    i = int(input()) - 1
    with open('deniro.csv', encoding='utf-8') as file:
        sorted_table = sorted(csv.reader(file), key=lambda x: int(x[i]) if x[i].isdigit() else x[i])
        [print(*l, sep=',') for l in sorted_table]


def csv_columns(filename):
    with open(filename, encoding='utf-8') as file:
        table = list(csv.reader(file))
    result = {key: [] for key in table[0]}
    for line in table[1:]:
        for i, key in enumerate(table[0]):
            result[key].append(line[i])
    return result


def domain_usage():
    with open('data.csv', encoding='utf-8') as file_in:
        table = list(csv.reader(file_in))
    domains = {}
    for line in table[1:]:
        domain_name = line[2].split('@')[1]
        domains[domain_name] = domains.get(domain_name, 0) + 1
    l = sorted(domains.items(), key=lambda x: (x[1], x[0]))

    with open('domain_usage.csv', 'w', encoding='utf-8', newline='') as file_out:
        writer = csv.writer(file_out)
        writer.writerow(('domain', 'count'))
        for row in l:
            writer.writerow(row)


def moscow_wifi():
    with open('wifi.csv', encoding='utf-8') as file_in:
        table = list(csv.reader(file_in, delimiter=';'))
    districts = {}
    for line in table[1:]:
        districts[line[1]] = districts.get(line[1], 0) + int(line[3])
    [print(*i, sep=": ") for i in sorted(districts.items(), key=lambda x: (-x[1], x[0]))]


def titanic_survivors():
    with open('titanic.csv', encoding='utf-8') as file_in:
        table = csv.reader(file_in, delimiter=';')
        survivors = list(filter(lambda x: x[0] == '1' and float(x[3]) < 18, table))
        [print(i[1]) for i in filter(lambda x: x[2] == 'male', survivors)]
        [print(i[1]) for i in filter(lambda x: x[2] == 'female', survivors)]


def usernames_log():
    from datetime import datetime
    with open('name_log.csv', encoding='utf-8') as file_in:
        table = csv.reader(file_in)
        headers = next(table)
        users = sorted(table, key=lambda x: datetime.strptime(x[2], '%d/%m/%Y %H:%M'))
        user_names = {}
        for user in users:
            user_names[user[1]] = (user[0], user[2])
    with open('new_name_log.csv', 'w', encoding='utf-8', newline='') as file_out:
        writer = csv.writer(file_out)
        writer.writerow(headers)
        for email, name in sorted(user_names.items()):
            writer.writerow((name[0], email, name[1]))


def condense_csv(filename, id_name):
    with open(filename, encoding='utf-8') as file_in:
        table = csv.reader(file_in)
        objects = {}
        headers = [id_name]
        for row in table:
            objects.setdefault(row[0], {})[row[1]] = row[2]
    with open('condensed.csv', 'w', encoding='utf-8', newline='') as file_out:
        writer = csv.writer(file_out)
        for i, obj in enumerate(objects.items()):
            if not i:
                headers.extend(obj[1].keys())
                writer.writerow(headers)
            row = [obj[0]]
            row.extend(obj[1].values())
            writer.writerow(row)

def students_count():
    with open('student_counts.csv', encoding='utf-8') as file_in:
        table = csv.DictReader(file_in)
        headers = [table.fieldnames[0]] + sorted(
            table.fieldnames[1:], key=lambda x: (int(x.split('-')[0]), x.split('-')[1]))
        with open('sorted_student_counts.csv', 'w', encoding='utf-8', newline='') as file_out:
            writer = csv.DictWriter(file_out, fieldnames=headers)
            writer.writeheader()
            writer.writerows(table)

def hungry_student():
    with open('prices.csv', encoding='utf-8') as file_in:
        table = csv.DictReader(file_in, delimiter=';')
        low_prices = []
        for row in table:
            lowest_item = min(row, key=lambda x: int(row[x]) if row[x].isdigit() else float('inf'))
            low_prices.append((row[lowest_item], lowest_item, row['Магазин']))
        product = sorted(low_prices)[0]
        print(product[1], product[2], sep=": ")