def solution(n, words):
    last = words[0]
    cnt = [0] * n
    cnt[0] += 1
    used = [words[0]]
    answer = []
    for i in range(1, len(words)):
        cnt[i%n] += 1
        if words[i] in used or words[i][0] != last[-1]:
            answer.append(i%n+1)
            answer.append(cnt[i%n])
            return answer
        else:
            used.append(words[i])
            last = words[i]

    return [0,0]