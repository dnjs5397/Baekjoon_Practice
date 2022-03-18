def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
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
graph = [[0] for i in range(N+1)] 
visited = [False] * (N+1)
visited2 = [False] * (N+1)
for i in range(M):
    a, b = map(int, input().split(' '))
    if graph[a][0] == 0:
        graph[a][0] = b
    else:
        graph[a].append(b)
for i in graph:
    if len(i) == 1 and i[0] == 0:
        del i[0]
graph2 = graph
dfs(graph, V, visited)
print()
dfs(graph2, V, visited2)
