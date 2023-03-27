import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().split())
arr = [[] for i in range(N+1)]
for i in range(M):
    a,b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    
distance = [-1] * (N+1)

visit = deque([X])
distance[X] = 0

while visit:
    node = visit.popleft()
    
    for i in arr[node]:
        if distance[i] == -1:
            distance[i] = distance[node] + 1
            visit.append(i)
    

if K in distance:
    for i in range(N+1):
        if distance[i] == K:
            print(i)
else:
    print(-1)