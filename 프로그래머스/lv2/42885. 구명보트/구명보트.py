def solution(people, limit):
    cnt = 0
    people.sort()
    i, j = 0, len(people)-1
    while i <= j:
        cnt += 1
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
    return cnt