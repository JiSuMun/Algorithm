import sys
input = sys.stdin.readline
s = input().rstrip()
N = len(s)
s_li = []
for i in range(1, N-1):
    for j in range(i+1, N):
        ns = s[:i][::-1] + s[i:j][::-1] + s[j:][::-1]
        s_li.append(ns)
print(min(s_li)) # 사전 순으로 가장 앞선 단어 출력 => 가장 작은 단어 출력