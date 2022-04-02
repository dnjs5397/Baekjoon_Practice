import sys
sys.setrecursionlimit(100000)

M, N, K = map(int, input().split())

graph = [list([0] * N) for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = -1


def dfs(x,y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return
    graph[x][y] = -1
    dfs(x-1,y)
    dfs(x+1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    return
cnt = 0
for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            cnt += 1
            dfs(i,j)
            
print(cnt)