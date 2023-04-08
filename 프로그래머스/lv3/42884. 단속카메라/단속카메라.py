def solution(routes):
    last = -30001
    cnt = 0
    routes.sort(key=lambda x:x[1])
    for i in routes:
        if i[0] > last:
            cnt += 1
            last = i[1]
    return cnt