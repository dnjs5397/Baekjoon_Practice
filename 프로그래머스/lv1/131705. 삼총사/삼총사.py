import itertools

def solution(number):
    answer = 0
    arr = itertools.combinations(number, 3)
    for i in arr:
        if sum(i) == 0:
            answer += 1
    return answer