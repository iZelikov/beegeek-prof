from datetime import date, time
print(*(s.strftime('%d/%m/%Y') for s in sorted(date.fromisoformat(input()) for _ in range(int(input())))), sep="\n")
