import sys

N, L = map(int, input().split())
cnt = 0
start = 0
end = 0

arr = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    arr.append((a, b))

arr.sort(key=lambda x: x[0])
idx = 0
for s, e in arr:
    if s > e:
        continue

    if idx > s:
        s = idx

    while s < e:
        s += L
        cnt += 1
    idx = s

print(cnt)
