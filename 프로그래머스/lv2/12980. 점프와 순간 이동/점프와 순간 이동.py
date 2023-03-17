def solution(N):
    answer = 0 
    
    while(N):
        if N % 2 == 0:
            N /= 2
        else:
            N -= 1
            answer += 1
            
    return answer