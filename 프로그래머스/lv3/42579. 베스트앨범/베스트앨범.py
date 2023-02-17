def solution(genres, plays):
    res = []
    d1 = {}
    d2 = {}
    # 고유번호, 장르, 재생횟수
    for i, (j, l) in enumerate(zip(genres, plays)):
        if j not in d1: d1[j] = [(i, l)]
        else: d1[j].append((i, l))
        
        if j not in d2: d2[j] = l
        else: d2[j] += l
    for k, v in sorted(d2.items(), key = lambda x: x[1], reverse = True):
        for (i, l) in sorted(d1[k], key = lambda x: x[1], reverse = True)[:2]:
            res.append(i)
    return res