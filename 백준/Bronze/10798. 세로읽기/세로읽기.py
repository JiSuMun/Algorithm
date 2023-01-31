import sys
input = sys.stdin.readline
w_li = [[0]*15 for _ in range(5)]
for i in range(5):
    word = list(input().rstrip())
    for j in range(len(word)): w_li[i][j] = word[j]        
for i in range(15):
    for j in range(5):
        if w_li[j][i] == 0: continue
        else: print(w_li[j][i], end = '')