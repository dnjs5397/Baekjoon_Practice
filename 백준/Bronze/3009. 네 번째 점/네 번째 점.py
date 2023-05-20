dx = [0] * 1001
dy = [0] * 1001
for _ in range(3):
    x, y =  map(int, input().split())
    dx[x] += 1
    dy[y] += 1
ax, ay = 0, 0
for i in range(1001):
    if dx[i] == 1:
        ax = i
    if dy[i] == 1:
        ay = i

print(ax, ay)