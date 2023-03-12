def solution(k, score):
    answer = []
    honor = []
    honor.append(score[0])
    answer.append(score[0])
    for i in range(1, len(score)):
        if len(honor) < k:
            honor.append(score[i])
            answer.append(min(honor))
            honor.sort(reverse=True)
        else:
            if score[i] > min(honor):
                del(honor[-1])
                honor.append(score[i])
                honor.sort(reverse=True)
            answer.append(min(honor))
            
        
    return answer