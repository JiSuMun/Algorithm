import sys
input = sys.stdin.readline

arr = []
for _ in range(9):
    arr.append(list(map(int, input().split())))
a = 0
b = 0
m = -1
for i in range(9):
    for j in range(9):
        if arr[i][j] > m:
            m = arr[i][j]
            a = i + 1
            b = j + 1
print(m)
print(a, b)