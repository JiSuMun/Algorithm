def solution(sequence, k):
    answer = []
    n = len(sequence)
    start, end = 0, 0
    for i in range(n):
        while start < k and end < n:
            start += sequence[end]
            end += 1
        if start == k:
            answer.append((i, end-1))
        start -= sequence[i]
        
    return sorted(answer, key=lambda x: x[1]-x[0])[0]