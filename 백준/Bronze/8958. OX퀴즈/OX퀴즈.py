T = int(input())

for _ in range(1, T+1):
    result = 0
    combo = 0
    str = input()
    for i in str:
        if i == 'O':
            combo += 1   
        else:
            combo = 0
        result += combo
    print(result)  