def solution(s):
    ans = True
    res = []
    for i in s:
        if i == '(': res.append(i)
        else:
            if not res:
                ans = False
            else:
                res.pop()
    if res: ans = False
    return ans