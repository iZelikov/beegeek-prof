def iter_4():
    numbers = [100, 70, 34, 45, 30, 83, 12, 83, -28, 49, -8, -2, 6, 62, 64, -22, -19, 61, 13, 5, 80, -17, 7, 3, 21, 73,
               88, -11, 16, -22]
    num_iter = iter(numbers)
    for _ in range(4):
        n = next(num_iter)
    print(n)

def iter_last():
    numbers = [100, 70, 34, 45, 30, 83, 12, 83, -28, 49, -8, -2, 6, 62, 64, -22, -19, 61, 13, 5, 80, -17, 7, 3, 21, 73,
               88,
               -11, 16, -22]
    num_iter = iter(numbers)
    while True:
        try:
            n = next(num_iter)
        except StopIteration:
            print(n)
            break
