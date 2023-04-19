def solution(x, y, n):
    arr = [9999999] * (y+1)
    arr[x] = 0
    if x == y:
        return 0

    for i in range(x, y+1):
        if arr[i] == 9999999:
            continue

        if i + n <= y:
            arr[i+n] = min(arr[i+n], arr[i] + 1)

        if i * 2 <= y:
            arr[i*2] = min(arr[i*2], arr[i] + 1)

        if i * 3 <= y:
            arr[i*3] = min(arr[i*3], arr[i] + 1)

    if arr[y] == 9999999:
        return -1
    else:
        return arr[y]