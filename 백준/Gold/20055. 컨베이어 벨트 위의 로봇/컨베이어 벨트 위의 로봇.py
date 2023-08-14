N, K = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(len(arr)):
    arr[i] = ([arr[i], 0])


def turn():
    arr.insert(0, arr.pop())
    if arr[N-1][1] == 1:
        arr[N-1][1] = 0


def move():
    for i in range(N-2, -1, -1):
        if arr[i][1] == 1:
            if arr[i+1][1] == 0 and arr[i+1][0] > 0:
                arr[i][1] = 0
                arr[i+1][1] = 1
                arr[i+1][0] -= 1

    if arr[N-1][1] == 1:
        arr[N-1][1] = 0


def up():
    if arr[0][0] > 0:
        arr[0][0] = arr[0][0] - 1
        arr[0][1] = 1


def check():
    cnt = 0
    for belt in arr:
        if belt[0] == 0:
            cnt += 1
        if cnt >= K:
            return True

    return False


answer = 1
while (1):
    turn()
    move()
    up()
    if check():
        print(answer)
        break
    answer += 1
