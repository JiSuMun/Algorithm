import sys
input = sys.stdin.readline
arr = [[0]*100 for _ in range(100)] # 전부 0을 가지는 2차원 배열
P = int(input())
for _ in range(P):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            arr[i][j] = 1 # 0으로 도배된 101 *101 크기의 도화지에서 색종이 위치에 1표시
result = 0
for i in arr:
    result += sum(i) # 1 카운팅
print(result)