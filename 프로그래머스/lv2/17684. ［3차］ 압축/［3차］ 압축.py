def solution(msg):
    words = dict()
    for i in range(65, 91):
        words[chr(i)] = i-64
    answer = []
    cnt = 27
    word = ''
    i = 0
    while (i < len(msg)):
        w = msg[i]
        if i+1 >= len(msg):
            i += 1
            answer.append(words[w])
        else:
            for j in range(i+1, len(msg)):
                w += msg[j]
                if w in words:
                    if j == len(msg)-1:
                        answer.append(words[w])
                        i = len(msg)+1
                        break
                    continue
                else:
                    answer.append(words[w[:-1]])
                    words[w] = cnt
                    cnt += 1
                    i = j
                    break


    return answer
