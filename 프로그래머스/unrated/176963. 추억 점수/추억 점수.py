def solution(name, yearning, photo):
    a = dict()
    for i in range(len(name)):
        a[name[i]] = yearning[i]
    answer = []
    for i in photo:
        tmp = 0
        for j in i:
            if j in a:
                tmp += a[j]
        answer.append(tmp)

    return answer