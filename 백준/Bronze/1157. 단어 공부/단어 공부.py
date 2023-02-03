import sys
input = sys.stdin.readline
s = input().upper()
m_num = 0
for i in range(26):
    cnt = s.count(chr(i + 65))
    if m_num < cnt: m_num = cnt; m_char = chr(i + 65)        
    elif m_num == cnt: m_char = "?"
print(m_char)