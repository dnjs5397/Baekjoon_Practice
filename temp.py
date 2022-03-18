graph = [[0,1,1,1],
         [1,1,1,1],
         [1,1,1,1],
         [0,0,1,0]]
for i in range(1, len(graph)):
    for j in range(1, len(graph[0])):
        if graph[i][j] != 0:
            graph[i][j] = min(graph[i-1][j], graph[i][j-1], graph[i-1][j-1]) + 1
max = 0
for i in range(len(graph)):
    for j in range(len(graph[0])):
        if max < graph[i][j]:
            max = graph[i][j]


print(max*max)