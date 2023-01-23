def Prime():
    P = [False, False] + [True] * 10000
    for i in range(2, 101):
        if P[i] == True:
            for j in range(i+i, 10001, i):
                P[j] = False
    
    T = int(input())
    for _ in range(T):
        n = int(input())
        a, b = n//2, n//2
        for _ in range(10000):
            if P[a] and P[b]:
                print(a, b)
                break
            else:
                a -= 1
                b += 1
Prime()