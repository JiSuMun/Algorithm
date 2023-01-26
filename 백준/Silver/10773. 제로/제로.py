import sys
input = sys.stdin.readline
K = int(input())
def S():
    nums = []
    for _ in range(K):
        num = int(input())
        if num == 0:
            nums.pop()
        else:
            nums.append(num)
    
    print(sum(nums))
    
if __name__ == '__main__':
    S()