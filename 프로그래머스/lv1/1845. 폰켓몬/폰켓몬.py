def solution(nums):
    pon = set(nums)
    if len(nums) / 2 > len(pon):
        return len(pon)
    else: return len(nums) / 2