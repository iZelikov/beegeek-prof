from collections import ChainMap, defaultdict, OrderedDict, Counter


def get_all_values(chainmap: ChainMap, key) -> set:
    out = set()
    for d in chainmap.maps:
        if key in d:
            out.add(d.get(key))
    return out


def deep_update(chainmap: ChainMap, key, value):
    if not key in chainmap:
        chainmap[key] = value
        return
    for d in chainmap.maps:
        if key in d:
            d[key] = value


def get_value(chainmap: ChainMap, key, from_left: bool = True):
    for i in (range(len(chainmap.maps)-1,-1,-1), range(len(chainmap.maps)))[from_left]:
        if key in chainmap.maps[i]:
            return chainmap.maps[i][key]
