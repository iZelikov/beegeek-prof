import sys


def traffic(n: int):
    if n <= 0:
        return
    traffic(n-1)
    print('Не парковаться')

def my_range(n: int):
    if not n: return
    my_range(n - 1)
    print(n)

numbers = [243, -279, 395, 130, 89, 269, 861, 669, 939, 367, -46, 710, 841, -280, -244, 274, -132, 273, 418, 432, -341, 437, 360, 960, 195, 792, 106, 461, -35, 980, -80, 540, -358, 69, -26, -416, 597, 96, 533, 232, 755, 894, 331, 323, -383, -386, 231, 436, 553, 967, 166, -151, 772, 434, 325, 301, 275, 431, 556, 728, 558, 702, 463, 127, 984, 212, 876, -287, -16, -177, 577, 604, 116, 500, 653, 669, 916, 802, 817, 762, -210, -353, 144, -351, 777, 805, 692, 22, -303, 249, 190, 411, 236, -274, 174, 380, 71, 124, -85, 430]

def my_dict(n: int):
    if not n: return
    my_dict(n - 1)
    print(f'Элемент {n-1}: {numbers[n-1]}')


def print_reverse():
    s = int(input())
    if not s:
        print(s)
        return
    print_reverse()
    print(s)

def triangle_1(h):
    print('*'*h)
    if not h:
        return
    triangle_1(h-1)

def triangle_2(h):
    if not h:
        return
    triangle_2(h-1)
    print('*'*h)

def sand_clock(start, step=1, reverse=False):
    if not step:
        return
    length = start * 4
    print(" " * 2 * (step - 1) + str(step) * (length - 4 * (step - 1)))
    if step == start or reverse:
        sand_clock(start, step - 1, reverse=True)
    else:
        sand_clock(start, step + 1)

def print_digits_1(number: int):
    if number < 10:
        print(number)
    else:
        print(number%10)
        print_digits_1(number//10)

def print_digits(number: int):
    if number < 10:
        print(number)
    else:
        print_digits(number//10)
        print(number%10)