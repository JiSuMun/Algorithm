import sys
input = sys.stdin.readline
d = {1: 0, 2: 1}
def s(N):
    if N in d: return d[N]
    t = 1 + min(s(N//3) + N % 3, s(N//2) + N % 2)
    d[N] = t
    return t
print(s(int(input())))