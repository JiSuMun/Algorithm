T = int(input())
a = ['a', 'e', 'i', 'o', 'u']
for t in range(1, T+1):
    s = input().rstrip()
    for i in s:
        if i in a: s = s.replace(i, '')
    print(f'#{t} {s}')