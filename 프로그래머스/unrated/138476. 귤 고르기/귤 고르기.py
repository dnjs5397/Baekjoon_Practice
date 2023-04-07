def solution(k, tangerine):
    answer = []
    f = dict()
    for i in tangerine:
        if i not in f:
            f[i] = 1
        else:
            f[i] += 1
    result = 0
    cnt = 0
    answer = sorted((list(f.values())), reverse=True)
    for i in answer:
        result += 1
        cnt += i
        if cnt >= k:
            break

    return result