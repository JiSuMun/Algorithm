import sys
T = int(sys.stdin.readline())
for t in range(T):
    H, W, N = map(int, input().split())
    f = N % H
    cnt = (N // H) + 1
    if f == 0:
        f = H
        cnt -= 1
    print(f*100+cnt)