def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        res = sorted(array[commands[i][0]-1:commands[i][1]])
        answer.append(res[commands[i][2]-1])
    return answer
# def solution(array, commands):
#     answer = []
#     for i, j, k in commands:
#         answer.append(sorted(array[i-1:j])[k-1])
#     return answer