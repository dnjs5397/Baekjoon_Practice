import sys
sys.setrecursionlimit(100000)

R, C = map(int, input().split(' '))
graph = []
for _ in range(R):
    s = list(input())
    graph.append(s)
    
isin = []
alpha = [[0 for i in range(C)]for j in range(R)]
answer = []

def dfs(x,y, val):
    if x <= -1 or x >= R or y <= -1 or y >= C:
        return
    if graph[x][y] in isin:
        return
    isin.append(graph[x][y])
    val += 1
    alpha[x][y] = val
    answer.append(val)
    dfs(x-1,y, val)
    dfs(x+1,y, val)
    dfs(x,y-1, val)
    dfs(x,y+1, val)
    return

dfs(0,0,0)
print(max(answer))