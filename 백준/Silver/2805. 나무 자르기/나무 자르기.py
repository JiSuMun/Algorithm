import sys
input = sys.stdin.read().splitlines()
N,M = map(int,input[0].split())
tree = [int(i) for i in input[1].split()]
def sol(N, M , tree):
    ma = max(tree) - 1
    mi = 1
    mid = (ma + mi)//2
    while(ma >= mi):
        cnt = 0
        for i in tree:
            if(i - mid > 0): cnt += (i - mid)
        if(cnt >= M): mi = mid + 1
        else: ma = mid - 1
        mid = (ma + mi)//2
    return ma
print(sol(N, M ,tree))