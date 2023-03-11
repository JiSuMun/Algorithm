def solution(citations):
    citations.sort()
    for i, j in enumerate(citations):
        if j >= len(citations) - i: # h번 이상 인용된 논문이 h편 이상 
            return len(citations) - i # 이후의 값들은 남은 요소의 개수가 줄어들면서 더 이상 최댓값이 될 수 없음
    return 0

# def solution(citations):
#     citations.sort(reverse=True)
#     for i, j in enumerate(citations):
#         if i >= j:
#             return i
#     return len(citations)