import itertools
N, M = map(int, input().split())
maps = []
for _ in range(N):
    maps.append(list(map(int, input().split())))

house = []
chick = []

for i in range(N):
    for j in range(N):
        if maps[i][j] == 1:
            house.append([i, j])
        if maps[i][j] == 2:
            chick.append([i, j])

cc = list(itertools.combinations(chick, M))
answer = 214700000
for c in cc:
    cd_sum = 0
    for h in house:
        cd = 214700000
        for ch in c:
            cd = min(cd, abs(h[0]-ch[0]) + abs(h[1]-ch[1]))
        cd_sum += cd
    answer = min(cd_sum, answer)

print(answer)