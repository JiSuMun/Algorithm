T = int(input())
for _ in range(T):
    string = input().split()
    for str in string:
        print(str[::-1], end=' ')
    print()