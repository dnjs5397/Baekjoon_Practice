def solution(keymap, target):
    result = []
    dic = dict()
    for i in keymap:
         for j in range(len(i)):
            if i[j] not in dic:
                dic[i[j]] = j+1
            else:
                dic[i[j]] = min(dic[i[j]], j+1)

    for i in target:
        ans = 0
        for j in i:
            if j in dic:
                ans += dic[j]
            else:
                ans = 0
                break

        if ans == 0:
            result.append(-1)
        else:
            result.append(ans)

    return result