M, N, K = map(int, input().split())

graph = [list([0] * N) for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = -1


for i in graph:
    print(i)