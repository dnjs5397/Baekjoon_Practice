H, W = map(int, input().split())
arr = list(map(int, input().split()))

idx = 0
answer = 0
while (idx < len(arr)):
    val = -1
    for i in range(idx+1, len(arr)):
        if arr[i] >= arr[idx]:
            val = i
            break

    if val != -1:
        for j in range(idx+1, val):
            answer += arr[idx] - arr[j]
            arr[j] += arr[idx] - arr[j]

        idx = val
    else:
        idx += 1

idx = len(arr)-1
while (idx > 0):
    val = -1
    for i in range(idx-1, -1, -1):
        if arr[i] >= arr[idx]:
            val = i
            break

    if val != -1:
        for j in range(idx-1, val, -1):
            answer += arr[idx] - arr[j]

        idx = val

    else:
        idx -= 1

print(answer)
