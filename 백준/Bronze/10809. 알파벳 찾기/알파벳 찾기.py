import sys
si = sys.stdin.readline
S = si()
for s in range(97, 123):
    print(S.find(chr(s)), end=' ')