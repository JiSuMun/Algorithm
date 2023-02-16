import sys
input = sys.stdin.readline
a, b = map(int, input().split())
A = list(map(int, input().split()))
B = set(map(int, input().split())) 
li = sorted([i for i in A if i not in B])
print(len(li))
if len(li) != 0: print(*li)