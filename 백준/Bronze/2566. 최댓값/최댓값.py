import sys
input = sys.stdin.readline
m, a, b = -1, 0, 0
for i in range(9):
    li = list(map(int, input().split()))
    for j in range(9):
        if m < li[j]:
            m, a, b = li[j], i+1, j+1
print(m)
print(a, b)