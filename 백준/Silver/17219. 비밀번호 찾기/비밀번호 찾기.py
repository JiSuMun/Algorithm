import sys
input = sys.stdin.readline
N, M = map(int, input().split())
d = {}
for _ in range(N):
    a, p = input().rstrip().split()
    d[a] = p
for _ in range(M):
    k = input().rstrip()
    print(d[k])