def solution(number, k):
    answer = ''
    for i in number:
        while k > 0 and answer and answer[-1] < i:
            answer = answer[:-1]
            k -= 1
        answer += i
    return answer[:-k] if k > 0 else answer