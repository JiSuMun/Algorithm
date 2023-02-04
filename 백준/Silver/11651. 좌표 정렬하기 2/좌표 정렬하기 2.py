import sys
input = sys.stdin.readlines
def cond(dot):
    x, y = dot.split()
    return int(y) + int(x)/1000000
dots = sorted(input()[1:], key=lambda x: cond(x))
print(''.join(dots))