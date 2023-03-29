def solution(maps):
    queue = [(0,0)]
    dxdy = [(0,-1), (0, 1), (1, 0), (-1, 0)]
    answer = 0
    while queue:
        x,y = queue.pop(0) # 그냥 배열을 사용해도 괜찮으나 시간복잡도를 줄이기 위해서는 deque를 사용할 것 (import collections)
        for i in dxdy:
            tx, ty = x + i[0], y + i[1]
            if tx < 0 or ty < 0 or tx >= len(maps) or ty >= len(maps[0]):
                continue
            
            if maps[tx][ty] == 0:
                continue
            
            if maps[tx][ty] == 1:
                maps[tx][ty] = maps[x][y] + 1
                queue.append((tx,ty))
    if maps[len(maps)-1][len(maps[0])-1] == 1:
        return -1
    else:
        return maps[len(maps)-1][len(maps[0])-1]
