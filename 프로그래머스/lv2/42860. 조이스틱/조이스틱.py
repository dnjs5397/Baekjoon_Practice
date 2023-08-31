def solution(name):
    arr = []
    for i in name:
        arr.append(min(ord(i)-65, 27-(ord(i)-64)))
    answer = 0
    move = len(name)-1
    for i in range(len(name)):

        answer += arr[i]

        right = i+1
        while (right < len(name) and name[right] == 'A'):
            right += 1

        move = min(move, i*2+len(name)-right, i+2*(len(name)-right))

    answer += move
    return answer
