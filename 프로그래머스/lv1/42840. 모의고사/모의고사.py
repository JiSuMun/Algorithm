def solution(answers):
    a1, cnt1 = [1, 2, 3, 4, 5], 0
    a2, cnt2 = [2, 1, 2, 3, 2, 4, 2, 5], 0
    a3, cnt3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5], 0
    for i in range(len(answers)):
        idx1, idx2, idx3 = i%5, i%8, i%10
        if a1[idx1] == answers[i]: cnt1 += 1
        if a2[idx2] == answers[i]: cnt2 += 1
        if a3[idx3] == answers[i]: cnt3 += 1
    res = max(cnt1, cnt2, cnt3)
    result = []
    if res == cnt1: result.append(1)
    if res == cnt2: result.append(2)
    if res == cnt3: result.append(3)
    return result