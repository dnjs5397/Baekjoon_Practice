import sys
sys.setrecursionlimit(100000)

N, M = map(int, input().split(' '))
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split(' '))
    graph[a].append(b)
    graph[b].append(a)

visit = [False] * (N+1)
cnt = 0
def dfs(v):
    visit[v] = True
    
    for i in graph[v]:
        if not visit[i]:
            dfs(i)

for j in range(1, N+1):
    if visit[j] == False:
        cnt += 1
        dfs(j)        
print(cnt)