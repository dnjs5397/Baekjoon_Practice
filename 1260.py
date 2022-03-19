def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

def bfs(v):
    visited[v] = True
    queue = [v]
    while queue:
        node = queue.pop(0)
        print(node, end=' ')
        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
N, M, V = map(int, input().split(' '))
graph = [[] for _ in range(N+1)] 
visited = [False] * (N+1)
for _ in range(M):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)
print(graph)
for i in range(1, N+1):
    graph[i].sort()

print(graph)
# dfs(V)
# visited = [False] * (N+1)
# print()
# bfs(V)
