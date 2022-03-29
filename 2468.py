import sys
sys.setrecursionlimit(100000)

N = int(input())
maxh = 0
answer = 0
graph = []
for _ in range(N):
    tmp = list(map(int, input().split(' ')))
    maxh = max(maxh, max(tmp))
    graph.append(tmp)
cnt = 0
def dfs(x,y):
    global cnt
    if x <= -1 or x >= N or y <= -1 or y >= N:
        return
    if oxgraph[x][y] == True:
        oxgraph[x][y] = False
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
    return

for i in range(1, maxh+1):
    cnt = 0
    oxgraph = [[True for _ in range(N)] for __ in range(N)]
    for j in range(N):
        for k in range(N):
            if graph[j][k] <= i:
                oxgraph[j][k] = False
    
    for q in range(N):
        for w in range(N):
            if oxgraph[q][w] == True:
                cnt += 1
                dfs(q,w)
    
    if cnt >= 1:
        answer = max(answer, cnt)

print(answer)