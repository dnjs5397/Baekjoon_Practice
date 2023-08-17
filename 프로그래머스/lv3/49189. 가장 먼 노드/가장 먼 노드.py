def solution(n, vertex):
    answer = [21470000] * (n+1)
    arr = [[] for i in range(n+1)]
    for i in vertex:
        arr[i[0]].append(i[1])
        arr[i[1]].append(i[0])
    visit = [0] * (n+1)
    visit[1] = 1
    answer[1] = 0
    m = []
    m.append((1, 0))


    while (m):
        t = m.pop(0)
        for node in arr[t[0]]:
            if visit[node] == 0:
                m.append((node, t[1]+1))
                visit[node] = 1
                answer[node] = min(answer[node], t[1]+1)


    result = 0
    answer[0] = 0
    val = max(answer)
    for i in range(1, n+1):
        if answer[i] == val:
            result += 1

    return result
