def solution(tickets):
    air = dict()

    for t in tickets:
        if t[0] not in air:
            air[t[0]] = [t[1]]
        else:
            air[t[0]].append(t[1])

    for key in air.keys():
        air[key].sort(reverse=True)

    v = ['ICN']
    answer = []

    while v:
        now = v[-1]

        if now not in air or len(air[now]) == 0:
            answer.append(v.pop())
        else:
            v.append(air[now].pop())

    return (answer[::-1])
