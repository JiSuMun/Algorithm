T = int(input())
for t in range(1, T + 1):
    square = list(map(int, input().split()))
    for i in range(3):
        if square.count(square[i]) % 2 == 1:
            print(f'#{t} {square[i]}')
            break