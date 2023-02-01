import sys
dot = sys.stdin.readlines()[1:]
dot.sort(key=lambda x: int(x.split()[1]))
dot.sort(key=lambda x: int(x.split()[0]))
print(''.join(dot))