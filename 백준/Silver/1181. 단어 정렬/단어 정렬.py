import sys
input = sys.stdin.readline
N = int(input())
li = [input().rstrip() for _ in range(N)]
li = list(set(li))
li = sorted(li)
li.sort(key = len)
print(*li, sep='\n')