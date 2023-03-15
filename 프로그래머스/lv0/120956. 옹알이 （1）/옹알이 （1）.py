def solution(babbling):
    answer = 0
    a = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        for j in a:
            i = i.replace(j, ' ')
        i = i.replace(' ', '')
        if i == '':
            answer += 1
    return answer