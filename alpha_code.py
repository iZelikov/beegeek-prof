import sys
from datetime import datetime

prev_prev = int(sys.stdin.readline().strip())
prev = int(sys.stdin.readline().strip())
a_n = prev - prev_prev
g_n = prev / prev_prev
progressions = ("Не прогрессия", "Арифметическая прогрессия", "Геометрическая прогрессия")
a, g = 1, 2
for i in sys.stdin:
    current = int(i.strip())
    if current - prev != a_n: a = 0
    if current / prev != g_n: g = 0
    if not a and not g: break
    prev = current
print(progressions[a + g])
