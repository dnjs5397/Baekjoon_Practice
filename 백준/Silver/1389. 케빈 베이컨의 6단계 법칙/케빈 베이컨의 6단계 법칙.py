N, M = map(int, input().split())

friends = [[] for i in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

answer = []
for i in range(1, N+1):
    ch = [0] * (N+1)
    ch[i] = 1
    v = [(i, 0)]
    idx = 1
    while (v):
        vv = v.pop(0)
        for node in friends[vv[0]]:
            if ch[node] == 0:
                ch[node] = vv[1] + 1
                v.append((node, vv[1]+1))
    ch[i] = 0

    answer.append([sum(ch), i])

answer.sort(key=lambda x: x[1])
answer.sort(key=lambda x: x[0])

print(answer[0][1])