import sys
from collections import Counter
input = sys.stdin.readline
N = int(input())
n_li = sorted([int(input()) for _ in range(N)])
print(round(sum(n_li)/N))
print(n_li[N//2])
new = Counter(n_li).most_common()
if len(new) > 1 and new[0][1] == new[1][1]: print(new[1][0])
else: print(new[0][0])
print(max(n_li)-min(n_li))