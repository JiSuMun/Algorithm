def solution(name):
    answer = 0
    m_move = len(name) - 1
    for i, alpha in enumerate(name):
        up = ord(alpha) - ord('A')
        down = ord('Z') - ord(alpha) + 1
        answer += min(up, down)
        next = i+1
        while next < len(name) and name[next] == 'A':
            next += 1
        m_move = min(m_move, 2*i+len(name)-next, i+2*(len(name)-next))
    answer += m_move
    return answer