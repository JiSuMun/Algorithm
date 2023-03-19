from itertools import permutations
def prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

def solution(numbers):
    res = 0
    result = []
    for i in range(1, len(numbers) + 1):
        result.append(list(set(map(''.join, permutations(numbers, i)))))
    a = list(set(map(int, set(sum(result, [])))))
    
    for j in a:
        if prime(j) == True: res += 1
    return res