f = input()
a, b = map(int, input().split())
l = [eval(f) for x in range(a, b + 1)]
print(f"Минимальное значение функции {f} на отрезке [{a}; {b}] равно {min(l)}")
print(f"Максимальное значение функции {f} на отрезке [{a}; {b}] равно {max(l)}")
