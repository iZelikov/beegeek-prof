import re

print(sum(bool(re.search(r'beegeek', line, re.I)) for line in open(0)))