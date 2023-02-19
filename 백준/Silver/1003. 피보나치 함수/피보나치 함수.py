import sys
input = sys.stdin.readline
T = int(input())
d = [0] * 41 # 0 <= N <= 40
d[0] = [1, 0]; d[1] = [0, 1]
for i in range(2, 41):
    d[i] = [d[i-1][1], sum(d[i-1])]
for _ in range(T):
    N = int(input())
    print(*d[N])