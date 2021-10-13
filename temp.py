numbers = [1,2,3,4,6,7,8,0]

def solution(numbers):
    answer = 0
    for i in range(0,10):
        count = 0
        for j in range(len(numbers)):
            if ( i == numbers[j]):
                count += 1
        if (count == 0):
            answer += i
    return answer
    
solution(numbers)