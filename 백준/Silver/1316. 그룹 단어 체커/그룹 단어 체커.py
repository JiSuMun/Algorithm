N = int(input()) # 단어의 개수
result = N
for _ in range(N):
    s = input()
    for i in range(len(s)-1):
        if s[i] == s[i+1]: # 알파벳이 연속적이면 통과
            pass
        elif s[i] in s[i+1:]: # 알파벳이 연속적이지 않고, 뒤의 위치에 같은 알파벳이 있다면
            result -= 1 # 단어개수 -1
            break # 없으면 값이 다르게 나옴
print(result)
