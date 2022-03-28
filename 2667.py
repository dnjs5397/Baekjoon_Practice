N = int(input())
maplist = []
for _ in range(N):
    s = input()
    s = list(s)
    maplist.append(s)
cnt = 0
def dfs(x,y):
    global cnt
    if x <= -1 or x >= N or y <= -1 or y >= N:
        return
    if maplist[x][y] == '1':
        maplist[x][y] = '0'
        cnt += 1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
    return
answer = []
for i in range(N):
    for j in range(N):
        if maplist[i][j] == '1':
            cnt = 0
            dfs(i,j)
            answer.append(cnt)

print(len(answer))  
for i in sorted(answer):
    print(i)