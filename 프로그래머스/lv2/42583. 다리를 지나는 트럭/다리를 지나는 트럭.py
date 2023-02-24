from collections import deque
def solution(bridge_length, weight, truck_weights):
    d = deque(truck_weights)
    bridge = [0]*bridge_length
    sec = 0
    while bridge:
        sec += 1
        bridge.pop(0)
        if d:
            if sum(bridge) + d[0] <= weight:
                bridge.append(d.popleft())
            else:
                bridge.append(0)
    return sec