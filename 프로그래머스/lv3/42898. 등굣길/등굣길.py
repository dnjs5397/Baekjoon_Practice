def solution(m, n, puddles):
    arr = [[0 for i in range(m)] for j in range(n)]
    if m == 1 or n == 1:
        if len(puddles) > 0:
            return 0
        else:
            return 1
        
        
    for i in puddles:
        arr[i[1]-1][i[0]-1] = -1

    for i in range(m):
        if arr[0][i] == -1:
            break
        arr[0][i] = 1
    for i in range(n):
        if arr[i][0] == -1:
            break
        arr[i][0] = 1

        
        
    for i in range(1, n):
        for j in range(1, m):
            if arr[i][j] == -1:
                continue
            left = arr[i][j-1]
            right = arr[i-1][j]
            if left == -1 and right == -1:
                continue
            elif left == -1 or right == -1:
                arr[i][j] = left + right + 1
            else:
                arr[i][j] = left + right

    return (arr[-1][-1] % 1000000007)
