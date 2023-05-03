N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    tmp = arr[a-1:b]
    tmp.reverse()
    i = a-1
    for j in range(len(tmp)):
        arr[i] = tmp[j]
        i += 1

for i in arr:
    print(i, end=' ')