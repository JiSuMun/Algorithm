import sys
input = sys.stdin.readline
N, M = map(int, input().split())
tree = list(map(int, input().split()))
def sol(N, M , tree):
    ma = max(tree) - 1
    mi = 1
    mid = (ma + mi)//2
    while ma >= mi:
        cnt = 0
        for i in tree:
            if i - mid > 0:
                cnt += i - mid
        if cnt >= M:
            mi = mid + 1
        else:
            ma = mid - 1
        mid = (ma + mi)//2
    return print(ma)
sol(N, M ,tree)