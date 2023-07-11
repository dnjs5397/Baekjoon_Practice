import sys
sys.setrecursionlimit(10**4)

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
melting = set()
ar = [[0 for i in range(M)] for j in range(N)]


def melt():
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0:
                c = 0
                for k in range(4):
                    tx = i+dx[k]
                    ty = j+dy[k]
                    if 0 <= tx < N and 0 <= ty < M:
                        if arr[tx][ty] == 0:
                            c += 1
                melting.add((i, j, c))


def check(x, y):
    if ar[x][y] == 1:
        ar[x][y] = 0
        for k in range(4):
            tx = x+dx[k]
            ty = y+dy[k]
            if 0 <= tx < N and 0 <= ty < M:
                check(tx, ty)
    else:
        return


def ice():
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0:
                ar[i][j] = 1


def zero():
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0:
                return False
    return True


melting = set()
ar = [[0 for i in range(M)] for j in range(N)]
answer = 0

while (1):
    answer += 1
    melting.clear()
    for i in range(N):
        for j in range(M):
            ar[i][j] = 0
    melt()
    for i in melting:
        arr[i[0]][i[1]] -= i[2]
        if arr[i[0]][i[1]] < 0:
            arr[i[0]][i[1]] = 0
    ice()
    cnt = 0
    for i in range(N):
        for j in range(M):
            if ar[i][j] == 1:
                cnt += 1
                check(i, j)
    if cnt >= 2:
        print(answer)
        exit(0)
    if zero():
        print(0)
        exit(0)
