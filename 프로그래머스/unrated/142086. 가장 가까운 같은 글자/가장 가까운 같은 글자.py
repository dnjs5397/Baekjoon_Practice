def solution(s):
    a = {}
    answer = []
    for i in range(len(s)):
        if a.get(s[i]) is None:
            a[s[i]] = i
            answer.append(-1)
        else:
            answer.append(i-a[s[i]])
            a[s[i]] = i
    return answer