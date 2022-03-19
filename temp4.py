a = ["1","2","4","3","3","4","1","5"]
processes = ["read 1 3 1 2",
             "read 2 6 4 7",
             "write 4 3 3 5 2",
             "read 5 2 2 5",
             "write 6 1 3 3 9",
             "read 9 1 0 7"]
answer = ['' for _ in range(len(processes))]
process = []
ing = []
done = [0 for _ in range(len(processes))]
for i in processes:
    process.append(i.split(' '))
for i in range(len(process)):
    process[i].append(i)
wait = []
count = 0
while (process):
    count += 1
    for i in process:
        if count == int(i[1]):
            tmp = process.pop(0)
            if len(ing) == 0: # 처리중인것이 없으면
                if len(wait) == 0: # 대기중인것도 없으면
                    ing.append(tmp)
                else: # 대기중인게 있으면
                    wait.append(tmp)
            else: # 처리중인게 있으면
                if ing[0][0] == 'write':
                    wait.append(tmp)
                else:
                    if len(wait) == 0:
                        if tmp[0] == 'write':
                            wait.append(tmp)
                        else:
                            ing.append(tmp)
                    else:
                        wait.append(tmp)
            break

count = 0
isdone = False
while(len(set(done)) != 1 or list(set(done))[0] != 1):
    count += 1
    iswrite = False
    for i in ing: # n초 되는순간 진행중인거 처리
        if int(i[1])+int(i[2]) <= count:
            if done[i[-1]] == 0:
                index = i[-1]
                done[index] = 1
                if i[0] == 'read':
                    s = ''
                    for j in range(int(i[3]), int(i[4])+1):
                        s += a[j]
                    answer[i[5]] = s
                    isdone = True
                else:
                    for j in range(int(i[3]), int(i[4])+1):
                        a[j] = i[5]
                    isdone = True
        else:
            isdone = False
    
    if isdone == True:
        for i in range(len(wait)):
            if wait[i][0] == 'write':
                iswrite = True
                ing.append(wait.pop(i))
                break
        if iswrite == True:
                continue
        for _ in range(len(wait)):
            ing.append(wait.pop(0))

print(answer)
print(count)