N, M = map(int, input().split())

arr = []
dx = [1, 1, 1]
dy = [-1, 0, 1]
for _ in range(N):
    arr.append(list(map(int, input().split())))

answer = 214700000


def DFS(x, y, cost, idx):
    global answer
    if x == N:
        answer = min(answer, cost)
        return
    if x < 0 or x >= N or y < 0 or y >= M:
        return

    for i in range(3):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx <= N and 0 <= ty < M and i != idx:
            DFS(tx, ty, cost+arr[x][y], i)


for q in range(M):
    DFS(0, q, 0, -1)
print(answer)
