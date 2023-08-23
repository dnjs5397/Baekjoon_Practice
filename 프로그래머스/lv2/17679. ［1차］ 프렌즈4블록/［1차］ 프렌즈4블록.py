def solution(m, n, board):
    answer = 0
    arr = [[] for _ in range(n)]

    for i in range(n):
        for j in range(m-1, -1, -1):
            arr[i].append(board[j][i])

    ch = [[1 for i in range(m)] for j in range(n)]

    isok = True
    while (isok):
        isok = False
        for i in range(len(arr)-1):
            for j in range(len(arr[i])-1):
                if j+1 <= len(arr[i+1])-1:
                    if arr[i][j] == arr[i+1][j] == arr[i][j+1] == arr[i+1][j+1]:
                        isok = True
                        ch[i][j] = 0
                        ch[i+1][j] = 0
                        ch[i][j+1] = 0
                        ch[i+1][j+1] = 0

        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if ch[i][j] == 0:
                    ch[i][j] = 1
                    arr[i][j] = ''
                    answer += 1

        for i in range(len(arr)):
            idx = 0
            while (idx < len(arr[i])):
                if arr[i][idx] == '':
                    arr[i].pop(idx)
                    idx -= 1
                idx += 1

    return answer