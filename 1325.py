from collections import deque

N, M = map(int, input().split(' '))
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split(' '))
    graph[b].append(a)

com = [0] * (N+1)
cnt = 0

def dfs(v):
    visit = [False] * (N+1)
    visit[v] = True
    q = deque([v])
    cnt = 1
    while q:
        tmp = q.popleft()
        for i in graph[tmp]:
            if not visit[i]:
                q.append(i)
                visit[i] = True
                cnt += 1
    
    return cnt
            
answer = []
maxval = -1       
for k in range(1, N+1):
    val = dfs(k)
    if val > maxval:
        answer = [k]
        maxval = val
    elif val == maxval:
        answer.append(k)



for i in sorted(answer):
    print(i, end=' ')