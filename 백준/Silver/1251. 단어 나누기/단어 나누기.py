import sys
input = sys.stdin.readline
word = input().rstrip()
n = len(word)
ans = 'z' * n
for i in range(n - 2):
    t = word[:i + 1][::-1]
    for j in range(i + 1, n - 1):
        s = t + word[i + 1:j + 1][::-1] + word[j + 1:][::-1]
        if s < ans:
            ans = s
print(ans)