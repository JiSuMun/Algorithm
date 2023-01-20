#T = int(input())
#for t in range(1, T + 1):
#    square = list(map(int, input().split()))
#    for i in range(3):
 #      if square.count(square[i]) % 2 == 1:
 #           print(f'#{t} {square[i]}')
#            break
T = int(input())
for t in range(1, T+1):
    a, b, c = input().split()
    if a == b:
        r = c
    else:
        if a == c:
            r = b
        else:
            r = a
    print(f'#{t} {r}')