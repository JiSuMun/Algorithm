import sys
input = sys.stdin.readline

def fibo(N):   
    zero = [1, 0, 1]
    one = [0, 1, 1]
    if len(zero) <= N:
        for i in range(len(zero), N+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print(zero[N], one[N])

T = int(input())
for t in range(T):
    N = int(input())
    fibo(N)