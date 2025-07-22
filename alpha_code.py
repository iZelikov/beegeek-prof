def sum_digits(n: int):
    return n%10 + sum_digits(n // 10) if n > 9 else n

print(sum_digits(123456789))
