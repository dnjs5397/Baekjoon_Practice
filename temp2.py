a = ["1","2","4","3","3","4","1","5"]
answer = []
processes = ["read 1 3 1 2",
           "read 2 6 4 7",
           "write 4 3 3 5 2",
           "read 5 2 2 5",
           "write 6 1 3 3 9", 
           "read 9 1 0 7"]
process = []
ing = ''
for i in processes:
    process.append(i.split(' '))
# for i in process:
#     print(i)
wait = []
count = 0
end = 0
while(process or wait):
    iswrite = False
    count += 1
    if count == end:
        ing = ''
    for i in process:
        if int(i[1]) > count:
            break
        if count == int(i[1]): # 현재시간과 t1 값이 같으면 처리시작
            tmp = process.pop(0) # 처리목록 추출
            if len(wait) == 0: # 대기목록 없으면 바로 진행
                if ing == '': # 대기목록 없고 진행중인 작업이 없을 때 ####
                    if tmp[0] == 'read': # read 일 때
                        ing = 'read'
                        end = max(end, end+int(tmp[2]))
                        s = ''
                        for j in range(int(tmp[3]), int(tmp[4])+1):
                            s += a[j]
                        answer.append(s)
                    else: # write 일 때
                        ing = 'write'
                        end = count + tmp[2]
                        for j in range(int(tmp[3]), int(tmp[4])+1):
                            a[j] = tmp[5]
                elif ing == 'read': # 대기목록 없고 진행중인 작업이 read 일 때 ####
                    if tmp[0] == 'read': # read 일 때
                        ing = 'read'
                        end = max(end, end+int(tmp[2]))
                        s = ''
                        for j in range(int(tmp[3]), int(tmp[4])+1):
                            s += a[j]
                        answer.append(s)
                    else: # write 일 때
                        wait.append(tmp)
                else: # 대기목록 없고 진행중인 작업이 wrtie 일 때 ####
                    if tmp[0] == 'read': # read 일 때
                        wait.append(tmp)
                    else: # write 일 때
                        wait.append(tmp)
            break            
    # t1 조건에 맞는 작업 처리 후에
    # 대기열에 뭐 있으면 처리해야함
    if wait:
        if ing == '': # 처리중인게 없을 때
            for i in range(len(wait)): # write가 있으면 write 먼저 처리
                if wait[i][0] == 'write':
                    ing = 'write'
                    end = count + int(i[2])
                    for j in range(int(wait[i][3]), int(wait[i][4])+1):
                        a[j] = wait[i][5]
                    iswrite = True
                    del(wait[i])
                    break
            if iswrite == True:
                continue
            