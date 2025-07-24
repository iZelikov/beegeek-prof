def hash_as_key(objects):
    result ={}
    for obj in objects:
        key = hash(obj)
        if key not in result:
            result[key] = obj
        elif isinstance(result[key],list):
            result[key].append(obj)
        else:
            result[key] = [result[key], obj]
    return result

def eval_collection():
    code = eval(input())
    if isinstance(code, list):
        print(code[-1])
    elif isinstance(code, tuple):
        print(code[0])
    elif isinstance(code, set):
        print(len(code))



def eval_math():
    import sys
    l = []
    for code in sys.stdin:
        l.append(eval(code))
    print(max(l))

def f_x():
    f = input()
    a, b = map(int, input().split())
    l = [eval(f) for x in range(a, b + 1)]
    print(f"Минимальное значение функции {f} на отрезке [{a}; {b}] равно {min(l)}")
    print(f"Максимальное значение функции {f} на отрезке [{a}; {b}] равно {max(l)}")
