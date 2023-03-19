def division(n):
    li = []
    for i in range(1, n//2+1):
        if n % i == 0: li.append(i)
    li.append(n)  
    return li

def solution(brown, yellow):
    res = []
    n = brown + yellow
    k = division(n)
    for i in k:
        j = n // i
        if (j-2)*(i-2) == yellow: return [j, i]