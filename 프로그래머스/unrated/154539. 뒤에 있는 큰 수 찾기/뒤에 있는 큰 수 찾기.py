def solution(numbers):
    answer = []
    tmp = dict()
    for i in range(len(numbers)-1):
        value = -1
        t = numbers[i+1:]
        if max(t) < numbers[i]:
            answer.append(value)
            continue
            
        for j in range(i+1, len(numbers)):
            if numbers[i] < numbers[j]:
                value = numbers[j]
                break
        answer.append(value)
    answer.append(-1)
    return answer