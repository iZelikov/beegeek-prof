from collections import Counter

books = Counter(input().split())
profit = 0
for _ in range(int(input())):
    book, money = input().split()
    if books[book]:
        books -= Counter([book])
        profit +=int(money)

print(profit)



