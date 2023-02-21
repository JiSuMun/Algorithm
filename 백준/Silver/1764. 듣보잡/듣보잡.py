import sys
input = sys.stdin.readline
N, M  = map(int, input().split())
a = set(input().rstrip() for _ in range(N)) # 듣도 못한 사람
b = set(input().rstrip() for _ in range(M)) # 보도 못한 사람
res = []
cnt = 0
for i in a:
    if i in b: res.append(i); cnt += 1
    else: continue
print(cnt, *sorted(a & b), sep='\n')