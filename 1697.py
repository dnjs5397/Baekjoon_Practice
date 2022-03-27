from collections import deque

N, K = map(int, input().split(' '))
visit = [0] * 100001

def bfs():
    q = deque([N])
    while q:
        tmp = q.popleft()
        if tmp == K:
            return visit[tmp]
        for i in (tmp-1, tmp+1, tmp*2):
            if 0 <= i < 100001 and not visit[i]:
                visit[i] = visit[tmp] + 1
                q.append(i)
                
print(bfs())