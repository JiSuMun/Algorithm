# 하나의 기준보다 큰 사람이 몇 명인지만 새고, 출력하면 됨
import sys
input = sys.stdin.readline
N = int(input())
li = []
for _ in range(N):
    x, y = map(int, input().split())
    li.append((x, y))
for i in li:
    res = 1
    for j in li:
        if i[0] < j[0] and i[1] < j[1]:
            res += 1
    print(res, end = ' ')