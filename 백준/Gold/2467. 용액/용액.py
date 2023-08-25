N = int(input())
arr = list(map(int, input().split()))



left = 0
right = N-1
cnt = abs(arr[left] + arr[right])

minval = arr[left]
maxval = arr[right]

while (left < right):
    tmp = arr[left] + arr[right]
    if abs(tmp) < cnt:
        cnt = abs(tmp)
        minval = min(arr[left], arr[right])
        maxval = max(arr[left], arr[right])

        if cnt == 0:
            break

    if tmp < 0:
        left += 1
    else:
        right -= 1

print(minval, maxval)
