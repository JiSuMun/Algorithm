import sys
input=sys.stdin.readline
while True:
    s=input().rstrip()
    if s=='.':break
    if s.count('(') != s.count(')') or s.count('[') != s.count(']'): print('no'); continue
    a = ''
    for i in s:
        if i in '()[]':
            a += i
    while '()' in a or '[]' in a:
        if '()' in a: a = a.replace('()','')
        if '[]' in a: a = a.replace('[]','')
    if a == '': print('yes')
    else: print('no')