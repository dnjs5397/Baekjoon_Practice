T = int(input())
for _ in range(T):
    next = False

    n = int(input())

    a, b = map(int, input().split())
    sang = []
    sang.append((a, b))

    store = []
    for __ in range(n):
        x, y = map(int, input().split())
        store.append((x, y))
    ch = [0] * n
    t, tt = map(int, input().split())
    fest = (t, tt)

    while (sang):
        ok = sang.pop(0)
        if abs(ok[0]-fest[0]) + abs(ok[1]-fest[1]) <= 1000:
            print("happy")
            next = True
            break

        for i in range(n):
            if ch[i] == 0:
                if abs(store[i][0]-ok[0]) + abs(store[i][1]-ok[1]) <= 1000:
                    sang.append((store[i][0], store[i][1]))
                    ch[i] = 1
            else:
                pass

    if next:
        continue
    else:
        print("sad")
