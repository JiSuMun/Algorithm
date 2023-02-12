import sys
def sol():
    input = sys.stdin.readline
    N, M = map(int,input().split())
    dd = [0] + [input().strip() for i in range(N)]
    d = dict(zip(dd, range(N+1)))
    ans = [dd[int(t)] if (t:=input().strip()).isdigit() else str(d[t]) for i in range(M)]
    print("\n".join(ans))
sol()