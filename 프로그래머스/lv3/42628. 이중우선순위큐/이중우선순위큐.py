import heapq

def solution(operations):
    queue = []
    heapq.heapify(queue)

    for oper in operations:
        if oper[0] == 'I':
            heapq.heappush(queue, int(oper[2:]))
        else:
            if queue:
                if oper[2] == '-':
                    queue.pop(0)
                else:
                    queue.pop()
                    
    if queue:
        queue.sort()
        return [queue[-1], queue[0]]
    else:
        return [0,0]