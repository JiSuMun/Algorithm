from sys import stdin, stdout
input = stdin.readline
N = int(input())
stack = []
for _ in range(N):
    od = input().rstrip()   
    if od == 'pop':
        stdout.write(stack.pop()+'\n') if stack else stdout.write('-1\n')           
    elif od == 'size': stdout.write(str(len(stack))+'\n')
    elif od == 'empty':
        stdout.write('0\n') if stack else stdout.write('1\n')   
    elif od == 'top':
        stdout.write(stack[-1]+'\n') if stack else stdout.write('-1\n')
    else: stack.append(od.split()[1])