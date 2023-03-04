import sys

N, M, K, X = map(int ,input().split(' '))
graph = [[] for _ in range(N+1)]
distance = [-1] * (N+1)
for i in range(M):
    a, b = map(int, sys.stdin.readline().split(' '))
    graph[a].append(b)
distance[X] = 0
answer = []
tmp = []
tmp.append(X)
while tmp:
    town = tmp.pop(0) 
    for i in graph[town]:
        if distance[i] == -1:
            distance[i] = distance[town] + 1
            tmp.append(i)
                
check = False
for i in range(1, N+1):
    if distance[i] == K:
        print(i)
        check = True

if check == False:
    print(-1)