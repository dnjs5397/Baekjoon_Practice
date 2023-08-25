import heapq
H, W = map(int, input().split())

arr = [[] for i in range(H+1)]
dis = [214700000] * (H+1)
for _ in range(W):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))

q = []
dis[1] = 0
heapq.heappush(q, (0, 1))

while q:
    distance, n = heapq.heappop(q)
    if dis[n] < distance:
        continue

    for dd in arr[n]:
        ddd = distance + dd[1]
        if ddd < dis[dd[0]]:
            dis[dd[0]] = ddd
            heapq.heappush(q, (ddd, dd[0]))

print(dis[H])
