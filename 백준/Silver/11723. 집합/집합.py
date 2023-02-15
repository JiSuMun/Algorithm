import sys
input = sys.stdin.readline
M = int(input())
S = set()
for i in range(M):
    s = input().rstrip().split()
    if len(s) == 1: # all, empty
        if s[0] == 'all': S = set([i for i in range(1, 21)])
        else: S = set()
        continue
    a, x = s[0], int(s[1])
    if a == 'add': S.add(x)
    if a == 'remove': S.discard(x)
    if a == 'check': print(1 if x in S else 0)
    if a == 'toggle': S.discard(x) if x in S else S.add(x)