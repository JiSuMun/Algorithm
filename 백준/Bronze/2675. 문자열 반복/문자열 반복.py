T = int(input())

for _ in range(T):
    R, S = input().split()
    t = ''
    for i in S:
        t += int(R) * i
    print(t)