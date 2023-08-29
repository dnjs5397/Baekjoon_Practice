import sys
import heapq

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


idx = 1
while (1):
    n = int(input())
    v = []
    if n == 0:
        break
    arr = []
    for _ in range(n):
        arr.append(list(map(int, sys.stdin.readline().split())))
    dp = [[214700000 for i in range(n)] for j in range(n)]
    dp[0][0] = arr[0][0]
    heapq.heappush(v, (dp[0][0], 0, 0))

    while (v):
        d, x, y = heapq.heappop(v)
        if d < dp[x][y]:
            continue
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < n and 0 <= ty < n:
                if d+arr[tx][ty] < dp[tx][ty]:
                    dp[tx][ty] = d+arr[tx][ty]
                    heapq.heappush(v, (d+arr[tx][ty], tx, ty))

    print("Problem " + str(idx) + ": " + str(dp[-1][-1]))
    idx += 1
