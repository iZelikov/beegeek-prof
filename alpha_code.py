from collections import ChainMap, defaultdict, OrderedDict, Counter

n = int(input())
# msq = [int(c) for s in range(n) for c in input().split()]
# magic_set = set()
# for i in range(n):
#     magic_set.add(sum(msq[i*n:i*n+n]))
#     magic_set.add(sum(msq[i::n]))
# magic_set.add(sum(msq[::n+1]))
# magic_set.add(sum(msq[n-1:1-n:n-1]))
# print(["NO","YES"][len(magic_set)==1 and set(msq)=={(i+1) for i in range(n**2)}])

print(set(range(n ** 2)))