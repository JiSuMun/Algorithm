import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A = []
B = []
s_Arr = []

def sum(arr):
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    return arr

A = sum(A)
B = sum(B)

for i in range(N):
    s_Arr.append([x+y for x,y in zip(A[i], B[i])])

for i in s_Arr:
    for j in i:
        print(j, end = ' ')
    print()