def get_digits(number: int | float) -> list[int]:
    return list(map(int, str(number).replace('.', '')))


def top_grade(grades: dict[str, str | list[int]]) -> dict[str, str | int]:
    return {'name': grades['name'], 'top_grade': max(grades['grades'])}


def cyclic_shift(numbers: list[int | float], step: int) -> None:
    step = step % len(numbers)
    if step:
        numbers[:-step], numbers[-step:] = numbers[-step:], numbers[:-step]


def matrix_to_dict(matrix: list[list[int | float]]) -> dict[int, list[int | float]]:
    return {i: l for i, l in enumerate(matrix, 1)}
