import sys
m_li = sys.stdin.readlines()[1:]
m_li.sort(key = lambda x: int(x.split()[0]))
print(''.join(m_li))