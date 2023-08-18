def solution(want, number, discount):
    fruit = []
    for i in range(len(number)):
        fruit += [want[i]] * number[i]

    fruit.sort()
    cnt = 0
    for i in range(len(discount)+1-10):
        if sorted(discount[i:i+10]) == fruit:
            cnt += 1

    return cnt
