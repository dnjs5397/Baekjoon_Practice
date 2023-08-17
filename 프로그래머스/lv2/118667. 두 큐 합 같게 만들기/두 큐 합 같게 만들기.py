import collections

def solution(q1, q2):
    q1 = collections.deque(q1)
    q2 = collections.deque(q2)
    answer = 21470000

    sum1 = sum(q1)
    sum2 = sum(q2)
    cnt = 0
    while (1):
        if sum1 == sum2:
            answer = min(answer, cnt)

        if cnt > len(q1) + len(q2) + 1:
            break

        cnt += 1
        if sum1 > sum2:
            q2.append(q1.popleft())
            sum1 -= q2[-1]
            sum2 += q2[-1]
        else:
            q1.append(q2.popleft())
            sum1 += q1[-1]
            sum2 -= q1[-1]


    if answer == 21470000:
        return -1
    else:
        return answer