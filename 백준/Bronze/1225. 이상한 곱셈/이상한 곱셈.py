import sys
input = sys.stdin.readline
A, B = input().split()
A = list(map(int, A))
B = list(map(int, B))
print(sum(A)*sum(B))