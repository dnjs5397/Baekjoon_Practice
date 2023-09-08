from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
x, y = 0, 0
answer = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            x = i
            y = j
            arr[i][j] = 0
            break
    if arr[i][j] == 9:
        x = i
        y = j
        break

fish = 2
level = 2

v = deque([])
v.append((x, y, 0))

while (v):
    visit = [[0 for i in range(N)] for j in range(N)]
    eat = []
    while (v):
        node = v.popleft()
        visit[node[0]][node[1]] = 1
        for i in range(4):
            tx = node[0] + dx[i]
            ty = node[1] + dy[i]
            if 0 <= tx < N and 0 <= ty < N and visit[tx][ty] == 0:
                visit[tx][ty] = 1
                if arr[tx][ty] == fish or arr[tx][ty] == 0:
                    if eat == []:
                        v.append((tx, ty, node[2]+1))
                elif arr[tx][ty] < fish:
                    v.append((tx, ty, node[2]+1))
                    eat.append((tx, ty, node[2]+1))

    if eat == []:
        print(answer)
        exit(0)

    if len(eat) > 1:
        eat.sort(key=lambda x: x[1])
        eat.sort(key=lambda x: x[0])
        eat.sort(key=lambda x: x[2])

    x = eat[0][0]
    y = eat[0][1]
    answer += eat[0][2]
    arr[x][y] = 0
    level -= 1
    if level == 0:
        fish += 1
        level = fish
    v = deque([])
    v.append((x, y, 0))
