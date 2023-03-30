def solution(n, computers):
    arr = [ [] for i in range(n)]

    for i in range(len(computers)):
        for j in range(len(computers[0])):
            if i != j:
                if computers[i][j] == 1:
                    arr[i].append(j)

    result = 0
    v = [False] * n
    for i in range(n):
        if v[i] == False:
            result += 1
            v[i] = True

            visit = [i]
            while visit:
                node = visit.pop(0)
                for j in arr[node]:
                    if v[j] == False:
                        v[j] = True
                        visit.append(j)
    return result