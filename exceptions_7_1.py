def code_review():
    total = 0
    with open('data.txt', encoding='utf-8') as file:
        for _ in file.readlines():
            total += + 1
    print(total)

def swapcase_vowels(string):
    vowels = 'aeiouy'
    swapped_string = []

    for char in string:
        if char in vowels:
            char = char.upper()
        swapped_string += char

    return ''.join(swapped_string)


def code_review_3():
    a = input()
    b = input()
    numbers = []
    for i in range(int(a), int(b) + 1):
        if i % 7 == 0:
            numbers.append(i)
    print(numbers)

def get_max_index(numbers):
    return numbers.find(max(numbers))