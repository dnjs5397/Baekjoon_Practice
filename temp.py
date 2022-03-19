goods = ["abcdeabcd","cdabe","abce","bcdeab"]
answer = []
for i in goods:
    isdone = False
    for j in range(len(i)): # 문자열 길이만큼 반복
        tmp = []
        for k in range(len(i)-j): # 문자열 자르는 개수
            cnt = 0
            left = k
            right = left+j+1
            s = i[left:right]
            for q in goods:
                if s in q:
                    cnt += 1
                if cnt >= 2:
                    break
            if cnt == 1:
                tmp.append(s)
                isdone = True
        if isdone == True:
            answer.append(tmp)
            break
    if isdone == False:
        answer.append("None")   
core = []
for i in answer:
    if i != "None":
        tmp = sorted(list(set(i)))
        core.append(' '.join(tmp))
    else:
        core.append('None')
        
print(core)
