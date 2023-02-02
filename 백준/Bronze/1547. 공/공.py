import sys
input = sys.stdin.readline
M = int(input())
a = [0, 1, 0, 0]
for _ in range(M):
    X, Y = map(int, input().split())
    a[X], a[Y] = a[Y], a[X]
print(a.index(1))