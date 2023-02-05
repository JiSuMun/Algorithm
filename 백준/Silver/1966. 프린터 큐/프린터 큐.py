import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    li = list(map(int, input().split()))
    que = [(i, li[i]) for i in range(N)]
    li.sort(reverse = True)
    res = 0
    for el in li:
        while que[0][1] != el:
            tmp = que.pop(0)
            que.append(tmp)
        res += 1
        if que.pop(0)[0] == M:
            break
    print(res)