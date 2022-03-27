N = int(input())
graph = [[] for _ in range(N+1)]
M = int(input())
for i in range(M):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)


visit = [False] * (N+1)
answer = []
def dfs(v):
    visit[v] = True
    answer.append(v)
    for i in graph[v]:
        if not visit[i]:
            dfs(i)
            
dfs(1)
print(len(answer)-1)