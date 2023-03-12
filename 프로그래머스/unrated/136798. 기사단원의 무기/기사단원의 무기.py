def solution(number, limit, power):
    answer = []
    result = 0
    for i in range(number):
        count = 0 
        for j in range(1, int((i+1)**(1/2)) + 1):
            if (i+1) % j == 0:
                count += 1
                if (j**2) != (i+1):
                    count += 1
        answer.append(count)

    for i in answer:
        if i > limit:
            result += power
        else:
            result += i
    return result