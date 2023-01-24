import sys
input = sys.stdin.readline
m, a, b = 0, 0, 0
for i in range(9):
    li = list(map(int, input().split()))
    if max(li) > m:
        m = max(li)
        a = i
        b = li.index(m)
print(m)
print(a+1, b+1)