import sys
input = sys.stdin.readline
a, b = map(int, input().split())
A = set(map(int, input().split())) # len(A) = a
B = set(map(int, input().split())) # len(B) = b
li = []
for i in A:
    if i not in B: li.append(i)
print(len(li))
if len(li) != 0: print(*sorted(li))