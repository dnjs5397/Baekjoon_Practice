n, m = map(int, input().split())
arr = []


def back(s):
    if len(arr) == m:
        for i in arr:
            print(i, end=' ')
        print()
        return

    for i in range(s, n+1):
        if len(arr) > 0:
            if i >= arr[-1]:
                arr.append(i)
                back(s)
                arr.pop()
        else:
            arr.append(i)
            back(s)
            arr.pop()


back(1)
