T = int(input()) 

for t in range(1, T+1):
    nums = list(map(int,input().split()))
    
    print(f'#{t} {round(sum(nums) / len(nums))}') #round: 소수점 n번째 까지 표현하고 싶을 때: (값, n)
    
    pass