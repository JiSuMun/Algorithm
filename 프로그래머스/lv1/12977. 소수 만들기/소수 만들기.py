from itertools import combinations
def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False  
    return True

def solution(nums):
    cnt = 0
    c_nums = [i for i in combinations(nums, 3)]
    for i in c_nums:
        a = sum(i)
        if isPrime(a) == True: cnt += 1
    return cnt