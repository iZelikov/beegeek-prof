def get_max_index(numbers):
    max_index = 0
    max_value = numbers[0]

    for index, value in enumerate(numbers):
        if index >= max_value:
            max_index = index
            max_value = value

    return max_index