import copy
import sys
sys.setrecursionlimit(100000)
N = int(input())
graph = []

for _ in range(N):
    s = list(input())
    graph.append(s)

graph_rgb = copy.deepcopy(graph)
    

def dfs_R(x,y, map):
    if x <= -1 or x >= N or y <= -1 or y >= N:
        return
    if map[x][y] == 'R':
        map[x][y] = '-'
        dfs_R(x-1, y, map)
        dfs_R(x+1, y, map)
        dfs_R(x, y-1, map)
        dfs_R(x, y+1, map)
    return

def dfs_G(x,y, map):
    if x <= -1 or x >= N or y <= -1 or y >= N:
        return
    if map[x][y] == 'G':
        map[x][y] = '-'
        dfs_G(x-1, y, map)
        dfs_G(x+1, y, map)
        dfs_G(x, y-1, map)
        dfs_G(x, y+1, map)
    return

def dfs_B(x,y, map):
    if x <= -1 or x >= N or y <= -1 or y >= N:
        return
    if map[x][y] == 'B':
        map[x][y] = '-'
        dfs_B(x-1, y, map)
        dfs_B(x+1, y, map)
        dfs_B(x, y-1, map)
        dfs_B(x, y+1, map)
    return

def dfs_RG(x,y, map):
    if x <= -1 or x >= N or y <= -1 or y >= N:
        return
    if map[x][y] == 'R' or map[x][y] == 'G':
        map[x][y] = '-'
        dfs_RG(x-1, y, map)
        dfs_RG(x+1, y, map)
        dfs_RG(x, y-1, map)
        dfs_RG(x, y+1, map)
    return

answer1, answer2 = 0, 0
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'R':
            answer1 += 1
            dfs_R(i,j,graph)
        elif graph[i][j] == 'G':
            answer1 += 1
            dfs_G(i,j,graph)
        elif graph[i][j] == 'B':
            answer1 += 1
            dfs_B(i,j,graph)
            
for i in range(N):
    for j in range(N):
        if graph_rgb[i][j] == 'R' or graph_rgb[i][j] == 'G':
            answer2 += 1
            dfs_RG(i,j,graph_rgb)
        elif graph_rgb[i][j] == 'B':
            answer2 += 1
            dfs_B(i,j,graph_rgb)
            
print(answer1, answer2)