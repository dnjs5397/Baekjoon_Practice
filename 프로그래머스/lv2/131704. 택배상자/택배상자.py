from collections import deque

def solution(order):
    answer = 0
    length = max(order)
    order = deque(order)
    sub = deque([])
    box = 1
    while(order):
        if box == order[0]:
            box += 1
            order.popleft()
            answer += 1
        elif box < order[0]:
            sub.append(box)
            box += 1
        else:
            if sub[-1] == order[0]:
                answer += 1
                sub.pop()
                order.popleft()
            else:
                break
    
    return answer