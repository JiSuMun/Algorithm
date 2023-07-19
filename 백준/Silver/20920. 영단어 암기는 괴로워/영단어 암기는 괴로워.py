import sys
input = sys.stdin.readline
from collections import Counter

N, M = map(int, input().split())
d = Counter([i for _ in range(N) if len(i:= input().strip()) >= M])
# 알파벳 사전 순
res = sorted(list(d.keys()))
# 길이 순
res.sort(key=len, reverse=True)
# 빈도수
res.sort(key=d.get,reverse=True)
print('\n'.join(res))