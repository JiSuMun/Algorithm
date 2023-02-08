import sys
input = sys.stdin.readline
def sol(n_li):
    cnt = 1
    res = []
    stack = []
    for num in n_li:
        while cnt <= num:
            stack.append(cnt)
            res.append('+')
            cnt += 1
        if stack.pop() != num: return "NO"
        res.append('-')       
    return '\n'.join(res)

if __name__ == "__main__":
    n = int(input())
    n_li = [int(input()) for _ in range(n)]
    print(sol(n_li))