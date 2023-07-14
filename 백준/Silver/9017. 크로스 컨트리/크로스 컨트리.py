T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    teamNum = max(arr)
    ch = [0] * (teamNum + 1)
    for i in range(1, teamNum+1):
        if arr.count(i) == 6:
            ch[i] = 1
    team = [[] for i in range(teamNum+1)]
    idx = 1
    for i in range(n):
        if ch[arr[i]] == 1:
            team[arr[i]].append(idx)
            idx += 1

    minrank = 214700000
    minteam = 214700000
    minsum = 214700000
    for i in range(len(team)):
        if len(team[i]) == 6:
            if sum(team[i][:4]) < minsum:
                minsum = sum(team[i][:4])
                minteam = i
                minrank = team[i][4]

            elif sum(team[i][:4]) == minsum:
                if team[i][4] < minrank:
                    minteam = i

    print(minteam)
