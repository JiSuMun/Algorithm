def solution(clothes):
    c = {}
    for k, v in clothes:
        c[v] = c.get(v, 0) + 1
    res = 1
    for i in c:
        res *= (c[i] + 1)
    return res - 1