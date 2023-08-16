N, M = map(int, input().split())
arr = []
alpha = [0] * 26
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for _ in range(N):
    arr.append(list(input()))
a = []
answer = -1


def BFS(i, j, cnt, ch):
    global answer
    if ch[ord(arr[i][j])-65] == 1:
        answer = max(answer, cnt)
        return

    for k in range(4):
        tx = i + dx[k]
        ty = j + dy[k]
        if 0 <= tx < N and 0 <= ty < M:
            ch[ord(arr[i][j])-65] = 1
            BFS(tx, ty, cnt+1, ch)
            ch[ord(arr[i][j])-65] = 0


BFS(0, 0, 0, alpha)
print(answer)
