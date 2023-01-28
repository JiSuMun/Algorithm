import sys
while True:
    n=sys.stdin.readline().rstrip()
    if n == '0':
        break
    else:
        print("yes") if n == n[::-1] else print("no")