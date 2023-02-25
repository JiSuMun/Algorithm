# def solution(prices):
#     res = [0] * len(prices)
#     for i in range(len(prices)):
#         for j in range(i+1, len(prices)):
#             if prices[i] <= prices[j]:
#                 res[i] += 1
#             else:
#                 res[i] += 1
#                 break
#     return res
def solution(prices):
    res = [0] * len(prices)
    stack = []
    for i, price in enumerate(prices):
        while stack and price < prices[stack[-1]]:
            a = stack.pop()
            res[a] = i - a # 결과_가격이 떨어지지 않은 시간 저장
        stack.append(i) # 증가하는 시간을 stack에 저장
    while stack:
        a = stack.pop()
        res[a] = len(prices) - a - 1
    return res