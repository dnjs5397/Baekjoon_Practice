def DFS(x,y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    if maplist[x][y] == 1:
        maplist[x][y] = 0
        DFS(x-1, y)
        DFS(x,y-1)
        DFS(x+1,y)
        DFS(x,y+1)
        return True
    return False
    

T = int(input())
for k in range(T):
    answer = 0
    N, M, K = map(int, input().split(' '))
    maplist = [[0 for col in range(N)]for row in range(M)]
    for i in range(K):
        X, Y = map(int, input().split(' '))
        maplist[Y][X] = 1

    for i in range(M):
        for j in range(N):
            if DFS(i,j) == True:
                answer += 1
                
    print(answer)