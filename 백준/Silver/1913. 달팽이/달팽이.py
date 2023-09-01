N = int(input())
target = int(input())
a1, a2 = 0, 0
arr = [[0 for i in range(N)] for j in range(N)]
val = N * N

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
x, y = 0, 0
idx = 0
while (val > 0):
    arr[x][y] = val
    if val == target:
        a1, a2 = x, y
    if 0 <= x + dx[idx] < N and 0 <= y + dy[idx] < N and arr[x + dx[idx]][y + dy[idx]] == 0:
        x += dx[idx]
        y += dy[idx]
    else:
        idx = (idx+1) % 4
        x += dx[idx]
        y += dy[idx]
    val -= 1
for i in arr:
    print(*i)
print(a1+1, a2+1)
