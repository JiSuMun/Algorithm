import sys
input = sys.stdin.readline
def Prime():
    P = [False, False] + [True] * 10000
    for i in range(2, 101):
        if P[i] == True:
            for j in range(i+i, 10001, i):
                P[j] = False
    
    T = int(input())
    for _ in range(T):
        n = int(input())
        a = n//2
        b = a
        for _ in range(10000):
            if P[a] and P[b]:
                print(a, b)
                break
            a -= 1
            b += 1
Prime()