import sys
input = sys.stdin.readline
N = int(input())
space = [input().rstrip() for _ in range(N)]
res = [0, 0] # 가로 세로 결과
for i in range(N):
    a, b = 0, 0 # 가로 세로 
    for j in range(N):
        if space[i][j] == '.': a += 1
        else: a = 0
        if a == 2: res[0] += 1

        if space[j][i] == '.': b += 1
        else: b = 0
        if b == 2: res[1] += 1
print(*res)