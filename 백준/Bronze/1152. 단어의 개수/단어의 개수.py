import sys
input = sys.stdin.readline
s = input().strip()
print(s.count(" ") + 1) if s else print(0)