def solution(d, budget):
    answer = 0
    s = 0
    b = sorted(d)
    for i in b:
        if s+i > budget:
            break
        s += i
        answer += 1     
    return answer