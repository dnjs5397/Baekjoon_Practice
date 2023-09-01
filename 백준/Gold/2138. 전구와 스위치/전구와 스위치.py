N = int(input())
cur = list(map(int, input()))
target = list(map(int, input()))
answer1 = 214700000
answer2 = 214700000
tmp = cur[:]
cnt = 0
for i in range(1, N):
    if tmp[i-1] == target[i-1]:
        continue

    cnt += 1
    for j in range(i-1, i+2):
        if j < N:
            tmp[j] = 1 - tmp[j]

if tmp == target:
    answer1 = cnt


tmp = cur[:]
tmp[0] = 1 - tmp[0]
tmp[1] = 1 - tmp[1]
cnt = 1
for i in range(1, N):
    if tmp[i-1] == target[i-1]:
        continue

    cnt += 1
    for j in range(i-1, i+2):
        if j < N:
            tmp[j] = 1 - tmp[j]

if tmp == target:
    answer2 = cnt

if answer1 == answer2 and answer1==214700000:
    print(-1)
else:
    print(min(answer1, answer2))
