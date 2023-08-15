def solution(e):
    ee = e + e
    answer = set()
    for i in range(len(e)):
        for j in range(1, len(e)+1):
            answer.add(sum(ee[i:i+j]))

    return len(answer)