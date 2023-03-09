import sys
input = sys.stdin.readline
M = int(input())
N = int(input())
li = [1]*(N+1)
li[1] = 0
for i in range(2, int(N**0.5)+1):
    if li[i]:
        for j in range(i**2, N+1, i):
            li[j] = 0
li = [i for i in range(M, N+1) if li[i] == 1]
if sum(li) == 0: print(-1)
else:    
    print(sum(li))
    print(min(li))