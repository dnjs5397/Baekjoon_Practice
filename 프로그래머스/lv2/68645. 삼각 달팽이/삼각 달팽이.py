def solution(n):
    arr = []
    for i in range(1, n+1):
        arr.append([0]*i)
    maxcnt = n*(n+1)//2
    dx = [1, 0, -1]
    dy = [0, 1, -1]
    cnt = 1
    x, y = 0, 0
    idx = 0
    while (cnt <= maxcnt):
        arr[x][y] = cnt

        tx = x + dx[idx]
        ty = y + dy[idx]
        if 0 <= tx < n and 0 <= ty < len(arr[tx]) and arr[tx][ty] == 0:
            x, y = tx, ty
        else:
            idx += 1
            idx %= 3
            tx = x + dx[idx]
            ty = y + dy[idx]
            x, y = tx, ty
        cnt += 1

    answer = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            answer.append(arr[i][j])
    return (answer)