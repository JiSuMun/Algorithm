T = int(input())
for t in range(1, T+1):
    N = int(input())
    card = list(map(str, input().split()))
    res = []
    s, e = 0, (N+1)//2
    for i in range(N//2):
        res.append(card[s])
        res.append(card[e])
        s += 1
        e += 1
    if N % 2: res.append(card[N//2])
    print(f'#{t}', *res)