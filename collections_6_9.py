from collections import ChainMap, defaultdict, OrderedDict, Counter

def zoo_count():
    import json
    with open('zoo.json', encoding='utf8') as file:
        print(sum(ChainMap(*json.load(file)).values()))


def timur_i_tochka():
    from collections import Counter
    bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
    meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
    sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
    vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
    toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}
    ingredients = ChainMap(bread, meat, sauce, vegetables, toppings)
    order = Counter(input().split(','))
    spaces = len(max(order, key=len))
    check = [{'ing': f'{ing:{spaces}} x {count}', 'price': ingredients[ing], 'count': count}
             for ing, count in sorted(order.items())]
    total = f'ИТОГ: {sum(map(lambda x: x['price'] * x['count'], check))}р'
    line_length = max(max(map(lambda x: len(x['ing']), check)), len(total))
    [print(line['ing']) for line in check]
    print('-' * line_length)
    print(total)
