n, m = map(int, input().split())
arr = [0] * (m)
ch = [0] * (n+1)


def back(num):
    if num == m:
        for i in arr:
            print(i, end=' ')
        print()
        return

    for i in range(1, n+1):
        if ch[i] == 0:
            arr[num] = i
            ch[i] = 1
            back(num+1)
            ch[i] = 0


back(0)
