graph = [[0,0,0],
         [0,1,0],
         [1,0,1]]

val = 0

def dfs(x,y):
    global val
    if x <= -1 or x >= len(graph) or y <= -1 or y >= len(graph):
        return False
    
    if graph[x][y] == 0:
        val += 1
        graph[x][y] = 1
        
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False
result = 0
for i in range(3):
    for j in range(3):
        if dfs(i,j) == True:
            if val > result:
                result = val
        val = 0
        
print(result)