import sys
N, M  = map(int, input().split())
arr = sys.stdin.read().splitlines()
a = set(arr[:N])
b = set(arr[N:])
res = list(a & b)
print(len(res), *sorted(res))