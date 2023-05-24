N, M = map(int, input().split())
arr = set()
for _ in range(N):
    arr.add(input())
cnt = 0
for _ in range(M):
    t = input()
    if t in arr:
        cnt += 1

print(cnt)