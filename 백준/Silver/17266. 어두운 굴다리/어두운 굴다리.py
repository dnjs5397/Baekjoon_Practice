N = int(input())
M = int(input())
rago = list(map(int, input().split()))

l = 0
r = 100000
answer = 21470000
while (l <= r):

    i = (l+r)//2

    ar = []
    left = rago[0]-i
    right = rago[0]+i
    if left > 0:
        l = i + 1
        continue
    if left < 0:
        left = 0

    isok = False
    for j in range(1, M):
        tleft = rago[j] - i
        tright = rago[j] + i
        if tleft > right:
            l = i + 1
            isok = True
            break
        else:
            right = tright

    if isok:
        continue
    if right >= N:
        answer = min(answer, i)
        r = i - 1
    else:
        l = i + 1

print(answer)
