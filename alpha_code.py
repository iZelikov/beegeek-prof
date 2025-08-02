numbers = [1, 2, 3, 4, 5]

iterator = iter(numbers)

next(iterator)
next(iterator)

del numbers[0]
del numbers[1]

print(next(iterator))