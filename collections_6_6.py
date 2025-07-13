from collections import OrderedDict


def reverse_dict():
    data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе',
                        'AdmArea': 'Центральный административный округ', 'District': 'район Арбат',
                        'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})
    print(OrderedDict(reversed(data.items())))


def reorder_dict():
    data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе',
                        'AdmArea': 'Центральный административный округ', 'District': 'район Арбат',
                        'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})
    l = list(data.keys())
    for i in range(len(data) // 2):
        data.move_to_end(l[i])
        data.move_to_end(l[~i])
    print(data)


def custom_sort(ordered_dict, by_values=False):
    for k in sorted(ordered_dict.keys(), key=(None, ordered_dict.get)[by_values]):
        ordered_dict.move_to_end(k)
