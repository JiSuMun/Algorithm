import sys
input = sys.stdin.readline
def sor():
    N  = int(input())
    arr = [0]*10001

    for _ in range(N):
        num = int(input())
        arr[num] += 1 # arr[num]에 num이 들어온 개수 count 

    for i in range(len(arr)): 
        # arr[i]에 숫자가 들어왔다면 
        if arr[i] != 0:
            # arr[num]에 num이 들어온 개수 만큼 출력 
            for j in range(arr[i]): 
                sys.stdout.write(str(i) + '\n')
def main():
    sor()
if __name__ == '__main__':
    main()