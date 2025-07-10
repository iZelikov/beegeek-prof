import pickle


def calculate_sum(obj):
    obj_sum = 0
    if isinstance(obj, dict):
        obj_sum = sum(map(int, filter(lambda x: isinstance(x, int), obj.keys())))
    elif isinstance(obj, list):
        filtered = list(filter(lambda x: isinstance(x, int), obj)) or [0]
        obj_sum = max(filtered) * min(filtered)
    return obj_sum


with open(input(), 'rb') as file:
    check_sum = int(input())
    obj = pickle.load(file)
    obj_sum = calculate_sum(obj)
print(f"Контрольные суммы {"не " * obj_sum == check_sum}совпадают")

print(calculate_sum({}))
