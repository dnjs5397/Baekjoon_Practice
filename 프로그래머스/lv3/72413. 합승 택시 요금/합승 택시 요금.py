def solution(n, s, a, b, fares):
    INF = (n*100000)+1
    arr = [[INF for i in range(n+1)] for j in range(n+1)]

    for i in range(1, n+1):
        arr[i][i] = 0

    for i in fares:
        arr[i[0]][i[1]] = i[2]
        arr[i[1]][i[0]] = i[2]

    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                arr[j][k] = min(arr[j][k], arr[j][i]+arr[i][k])


    # if arr[s][a] != 0 and arr[s][b] != 0:
    #     answer = arr[s][a] + arr[s][b]
    # else:
    answer = INF

    for i in range(n+1):
        if (arr[s][i] != INF and arr[i][a] != INF and arr[i][b] != INF):
            answer = min(answer, arr[i][s] + arr[i][a] + arr[i][b])

    return answer