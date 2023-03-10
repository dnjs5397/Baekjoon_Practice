def solution(food):
    answer = ''
    for i in range(1, len(food)):
        if food[i] % 2 != 0:
            food[i] -= 1
        answer += str(i) * (food[i]//2)
    
    answer2 = answer[::-1]
    answer = answer + '0' + answer2
    return answer