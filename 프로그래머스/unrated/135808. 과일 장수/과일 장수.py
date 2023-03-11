def solution(k, m, score):
    
    result = 0
    score.sort(reverse=True)
    i = 0
    while(i+m <= len(score)):
        result += score[i+m-1] * m
        i += m


    return result