N = int(input())
list = []
for i in range(N):
    n = int(input())
    list.append(n)
one = list.count(1)
zero = list.count(0)
if one > zero:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')