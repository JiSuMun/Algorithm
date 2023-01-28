def pelindrome(num):
    N = len(num)
    for i in range(N//2):
        if num[i] != num[N-1-i]:
            return 'no'
    return 'yes'

while True:
    num = int(input())
    if num == 0:
        break
    print(pelindrome(str(num)))