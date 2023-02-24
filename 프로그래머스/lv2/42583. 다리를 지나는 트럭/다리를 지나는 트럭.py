# from collections import deque
# def solution(bridge_length, weight, truck_weights):
#     d = deque(truck_weights)
#     bridge = [0]*bridge_length
#     sec = 0
#     while bridge:
#         sec += 1
#         bridge.pop(0)
#         if d:
#             if sum(bridge) + d[0] <= weight:
#                 bridge.append(d.popleft())
#             else:
#                 bridge.append(0)
#     return sec

from collections import deque
def solution(bridge_length, weight, truck_weights):
    d = deque([0] * bridge_length) # 다리 위에 있는 트럭
    wei = deque(truck_weights) 
    sec = 0 
    bridge = 0 # 다리 위에 올라가있는 무게
    while d: 
        sec += 1 
        a = d.popleft() 
        bridge -= a
        if wei: 
            if bridge + wei[0] <= weight: 
                b = wei.popleft() 
                bridge += b
                d.append(b) 
            else: d.append(0) 
    return sec