import sys
sys.setrecursionlimit(1000000) # 재귀 깊이 정해주기 백만까지 가능 / 설정 안하면 998까지

# def DFS(x,y):
#     if x <= -1 or x >= M or y <= -1 or y >= N:
#         return False
#     if maplist[x][y] == 1:
#         maplist[x][y] = 0
#         DFS(x-1, y)
#         DFS(x+1,y)
#         DFS(x,y-1)
#         DFS(x,y+1)
#         return True
#     return False
    

# T = int(input())
# for k in range(T):
#     answer = 0
#     N, M, K = map(int, input().split(' '))
#     maplist = [[0 for col in range(N)]for row in range(M)]
#     for i in range(K):
#         X, Y = map(int, input().split(' '))
#         maplist[Y][X] = 1

#     for i in range(M):
#         for j in range(N):
#             if DFS(i,j) == True:
#                 answer += 1
                
#     print(answer)

n = int(input())
for _ in range(n):
    M, N, K = map(int, input().split(' '))
    graph = [[0 for i in range(M)] for j in range(N)]
    for i in range(K):
        x,y = map(int, input().split(' '))
        graph[y][x] = 1

    def dfs(x,y):
        if x <= -1 or x >= M or y <= -1 or y >= N:
            return False
        if graph[y][x] == 1:
            graph[y][x] = 0
            dfs(x-1,y)
            dfs(x+1,y)
            dfs(x,y-1)
            dfs(x,y+1)
            return True
        return False
    cnt =0 
    for i in range(N):
        for j in range(M):
            if graph[i][j] == True:
                cnt += 1

    print(cnt)