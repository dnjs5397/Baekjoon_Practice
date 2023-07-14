N = int(input())
sw = list(map(int, input().split()))

st = int(input())
for _ in range(st):
    a, b = map(int, input().split())
    idx = b-1
    if a == 1:
        while (idx < N):
            if sw[idx] == 0:
                sw[idx] = 1
            else:
                sw[idx] = 0
            idx += b

    else:
        arr = [b-1]
        left = b-2
        right = b
        while (left >= 0 and right < N):
            if sw[left] == sw[right]:
                arr.append(left)
                arr.append(right)
                left -= 1
                right += 1
            else:
                break

        for i in arr:
            if sw[i] == 0:
                sw[i] = 1
            else:
                sw[i] = 0

idx = 0
while (1):
    print(*sw[idx:idx+20])
    if idx >= N:
        break
    else:
        idx += 20
