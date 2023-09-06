import copy
import itertools

N, M = map(int, input().split())

maps = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]
for _ in range(N):
    maps.append(list(map(int, input().split())))
answer = 0
xy = []
for i in range(N):
    for j in range(M):
        if maps[i][j] == 0:
            xy.append((i,j))

v = list(itertools.combinations(xy, 3))

def DFS(arr,x,y):
    for i in range(4):
        tx = x+dx[i]
        ty = y+dy[i]
        if 0<=tx<N and 0<=ty<M:
            if arr[tx][ty] == 0:
                arr[tx][ty] = 2
                DFS(arr, tx, ty)

def count(arr):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                cnt += 1
    return cnt

for node in v:
    tmp = copy.deepcopy(maps)
    tmp[node[0][0]][node[0][1]] = 1
    tmp[node[1][0]][node[1][1]] = 1
    tmp[node[2][0]][node[2][1]] = 1
    
    for i in range(N):
        for j in range(M):
            if tmp[i][j] == 2:
                DFS(tmp, i,j)
    
    answer = max(answer, count(tmp))

print(answer)