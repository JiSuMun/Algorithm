import sys
input = sys.stdin.readline
N, M = map(int, input().split())
d = dict(input().rstrip().split() for _ in range(N))
res = [d[input().rstrip()] for _ in range(M)]
print('\n'.join(res))