import sys
input = sys.stdin.readline
s = input().rstrip()[::-1]
n = len(s)
print(min(s[j:]+s[i:j]+s[:i] for i in range(1,n) for j in range(i+1,n)))