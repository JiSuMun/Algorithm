import sys
input = sys.stdin.readline
res = 0
p_li = []
for _ in range(4):
    a, b = map(int, input().split())
    res = res - a + b
    p_li.append(res)
print(max(p_li))