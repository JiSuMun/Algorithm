from itertools import product
def solution(word):
    res = []
    alpha = ['A', 'E', 'I', 'O', 'U']
    for i in range(1, 6):
        for j in product(alpha, repeat=i):
            res.append(''.join(j))
    res.sort()
    return res.index(word) + 1