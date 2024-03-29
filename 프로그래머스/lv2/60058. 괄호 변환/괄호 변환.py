def solution(p):
    res = ''
    if len(p) == 0 or isRight(p) == True: return p
    else:
        u, v = isBalance(p)
        if isRight(u) == True:
            res += u
            res += solution(v)
            return res
        else:
            res += "("
            res += solution(v)
            res += ")"
            a = ""
            for i in u[1:-1]:
                if i == "(": a += ")"
                else: a += "("
            res += a
            return res

def isBalance(p):
    l_cnt, r_cnt = 0, 0
    for i in p:
        if i == "(": l_cnt += 1
        else: r_cnt += 1
        if r_cnt != 0 and l_cnt == r_cnt:
            idx = l_cnt + r_cnt
            u, v = p[:idx], p[idx:]
            return u, v

def isRight(p):
    li = []
    for i in p:
        if i == "(": li.append(i)
        else:
            if len(li) == 0: return False
            li.pop()
    if len(li) > 0: return False
    else: return True