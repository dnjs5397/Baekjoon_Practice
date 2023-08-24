idx = 1
while (1):
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        exit(0)

    answer = (V // P) * L
    answer += min(L, V % P)
    print("Case " + str(idx) + ": " + str(answer))
    idx += 1
