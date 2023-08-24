n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(input()))

for i in range(n):
    for j in range(m):
        arr[i][j] = int(arr[i][j])
for i in range(n-1):
    for j in range(m-1):
        if arr[i][j] == 0:
            continue

        if arr[i+1][j] > 0 and arr[i][j+1] > 0 and arr[i+1][j+1] > 0:
            arr[i+1][j+1] = min(arr[i][j], arr[i][j+1], arr[i+1][j]) + 1

answer = -1
for i in arr:
    answer = max(answer, max(i))
print(answer*answer)