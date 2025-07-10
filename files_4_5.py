import pickle


def wrong_dump():
    dogs = {'Ozzy': 2, 'Filou': 7, 'Luna': 4, 'Skippy': 11, 'Barco': 13, 'Balou': 10, 'Laika': 15}
    with open('dogs.pkl', 'wb') as file:
        pickle.dump(dogs, file)


def pickle_this():
    import sys
    with open(input(), 'rb') as file:
        my_func = pickle.load(file)
        args = [arg.strip() for arg in sys.stdin]
        print(my_func(*args))


def filter_dump(filename, objects, typename):
    filtered = list(filter(lambda x: type(x) == typename, objects))
    with open(filename, 'wb') as p_file:
        pickle.dump(filtered, p_file)

def check_sum_pickle():
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
