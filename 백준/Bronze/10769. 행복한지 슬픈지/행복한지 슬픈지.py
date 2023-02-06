import sys
input = sys.stdin.readline
s = input().rstrip()
happy = s.count(':-)')
sad = s.count(':-(')
if (happy, sad) == (0, 0): print('none')
elif happy > sad: print('happy')
elif happy < sad: print('sad')
else: print('unsure')