import sys
input = sys.stdin.readline
sq = [[0]*100 for _ in range(100)]
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2): sq[i][j] = 1           
res = 0
for k in sq: res += sum(k)  
print(res)