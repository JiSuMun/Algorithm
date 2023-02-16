def solution(phone_book):
    res = True
    p = sorted(phone_book)
    for i in range(len(p)-1):
        if p[i] == p[i+1][:len(p[i])]:
            res = False
            break
    return res