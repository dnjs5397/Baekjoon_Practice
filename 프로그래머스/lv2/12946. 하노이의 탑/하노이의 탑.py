def solution(n):
    answer = []
    def hanoi(n, pre, next, middle):

        if n == 1:
            answer.append([pre, next])
            return

        hanoi(n-1, pre, middle, next)
        answer.append([pre, next])
        hanoi(n-1, middle, next, pre)
    
    hanoi(n, 1,3,2)
    return answer
