def dfs(numbers, target, c_sum, idx):
    if idx == len(numbers):
        if c_sum == target:
            return 1
        else:
            return 0
    else:
        return dfs(numbers, target, c_sum + numbers[idx], idx+1) + dfs(numbers, target, c_sum - numbers[idx], idx+1)

def solution(numbers, target):
    answer = dfs(numbers, target, 0, 0)
    return answer