def solution(rows, columns, queires):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    arr = [[0 for i in range(columns)] for j in range(rows)]
    c = 1
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = c
            c += 1
    answer = []

    for q in queires:
        tt = []
        x, y = q[0]-1, q[1]-1
        stack = [(q[0]-1, q[3]-1), (q[2]-1, q[3]-1), (q[2]-1, q[1]-1)]
        idx = 0
        tt.append(arr[x][y])
        while (1):
            if stack and x == stack[0][0] and y == stack[0][1]:
                idx += 1
                stack.pop(0)

            tx = x + dx[idx]
            ty = y + dy[idx]
            if tx == q[0]-1 and ty == q[1]-1:
                break
            tt.append(arr[tx][ty])
            x = tx
            y = ty

        answer.append(min(tt))
        tt.insert(0, tt.pop())

        x, y = q[0]-1, q[1]-1
        stack = [(q[0]-1, q[3]-1), (q[2]-1, q[3]-1), (q[2]-1, q[1]-1)]
        idx = 0
        cnt = 1
        arr[x][y] = tt[0]
        while (1):
            if stack and x == stack[0][0] and y == stack[0][1]:
                idx += 1
                stack.pop(0)

            tx = x + dx[idx]
            ty = y + dy[idx]
            if tx == q[0]-1 and ty == q[1]-1:
                break
            arr[tx][ty] = tt[cnt]
            cnt += 1
            x = tx
            y = ty


    return answer
