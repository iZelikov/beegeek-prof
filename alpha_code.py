import csv

with open('prices.csv', encoding='utf-8') as file_in:
    table = csv.DictReader(file_in, delimiter=';')
    low_prices = []
    for row in table:
        lowest_item = min(row, key= lambda x: int(row[x]) if row[x].isdigit() else float('inf'))
        low_prices.append((row[lowest_item], lowest_item, row['Магазин']))
    product = sorted(low_prices)[0]
    print(product[1], product[2], sep=": ")