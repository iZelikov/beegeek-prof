import re

start, end = map(int, input().split())
pattern = re.compile(r'\d+')
print(sum(map(int,pattern.findall(input(), pos=start, endpos=end))))