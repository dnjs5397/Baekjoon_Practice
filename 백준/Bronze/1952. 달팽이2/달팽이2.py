N, M = map(int, input().split())

arr = [[0 for i in range(M)] for j in range(N)]
val = M * N
cnt = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
x, y = 0, 0
idx = 0
while (val > 0):
    arr[x][y] = val
    if 0 <= x + dx[idx] < N and 0 <= y + dy[idx] < M and arr[x + dx[idx]][y + dy[idx]] == 0:
        x += dx[idx]
        y += dy[idx]
    else:
        cnt += 1
        idx = (idx+1) % 4
        x += dx[idx]
        y += dy[idx]
    val -= 1

print(cnt-1)
