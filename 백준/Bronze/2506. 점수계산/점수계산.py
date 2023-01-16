N = int(input())
nums_list = list(map(int, input().split()))
result=0
combo = 0

for i in range(N):
    if nums_list[i] == 1:
        combo += 1   
    else:
        combo = 0
    result += combo
print(result)