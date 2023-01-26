import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    PS = input().rstrip()
    while '()' in PS:
        PS = PS.replace('()', '')       
    if PS == '':
        print('YES')
    else:
        print('NO')