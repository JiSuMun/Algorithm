# n을 반으로 나누고 각자 +1, -1해보면서 두 수가 모두 소수인지 확인함
from math import sqrt
def Prime(n):
    if n == 1: return False
    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0: return False
    return True

for _ in range(1, int(input())+1):
    n = int(input())
    a, b = n//2, n//2
    while a > 0:
        if Prime(a) and Prime(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1