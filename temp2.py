N = int(input()) # 스테이지 개수
stages = [4,4,4,4] # 멈춰있는 스테이지 번호

def solution(N, stages):
    player = len(stages)
    stay = list(0 for i in range(N+2))
    answer = []

    for i in range(player):
        stay[stages[i]] += 1
    
    for i in range(1,N+1):
        if (stay[i] == 0):
            answer.append(0.0)
        else:
            answer.append(stay[i] / player)
            player -= stay[i]

    answer = sorted(range(len(answer)), key=answer.__getitem__, reverse=True)
    for i in range(len(answer)):
        answer[i] += 1

    return answer
