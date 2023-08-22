def solution(n, wires):
    answer = 214700000
    for i in range(len(wires)):
        arr = [[] for _ in range(n+1)]
        for j in range(len(wires)):
            if j != i:
                arr[wires[j][0]].append(wires[j][1])
                arr[wires[j][1]].append(wires[j][0])

        ch = [0] * (n+1)
        ch[1] = 1
        v = [1]
        cnt = 1
        while (v):
            node = v.pop(0)
            for nod in arr[node]:
                if ch[nod] == 0:
                    ch[nod] = 1
                    v.append(nod)
                    cnt += 1
        answer = min(answer, abs((n-cnt)-cnt))

    return answer