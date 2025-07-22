def recursive_sum(nested_lists):
    sum = 0
    for item in nested_lists:
        if isinstance(item, int):
            sum += item
        else:
            sum += recursive_sum(item)
    return sum


def linear(nested_lists):
    return sum(map(lambda x: linear(x) if isinstance(x, list) else [x], nested_lists), [])


def get_value(nested_dicts, key):
    for k, v in nested_dicts.items():
        if k == key:
            return v
        elif isinstance(v, dict):
            result = get_value(v, key)
            if not result is None:
                return result


def get_all_values(nested_dicts, key):
    result = set()
    for k, v in nested_dicts.items():
        if k == key:
            result.add(v)
        elif isinstance(v, dict):
            find = get_all_values(v, key)
            if isinstance(find, set):
                result.update(find)
    return result


def dict_travel(nested_dicts):
    def rec(dicts):
        keys = {}
        for k1, v1 in dicts.items():
            if isinstance(v1, dict):
                result = rec(v1)
                for k2, v2 in result.items():
                    keys['.'.join([k1, k2])] = v2
            else:
                keys[k1] = v1
        return keys

    [print(f'{k}: {v}') for k, v in sorted(rec(nested_dicts).items())]