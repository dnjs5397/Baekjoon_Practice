def solution(files):
    def divide(file):
        file = file.upper()
        idx = []
        gogo = True
        cnt = 0
        for i in range(len(file)):
            if gogo:
                if 48 <= ord(file[i]) <= 57:
                    idx.append(i)
                    cnt += 1
                    gogo = False
                    continue
            else:
                if 48 <= ord(file[i]) <= 57 and 0 < cnt < 6:
                    cnt += 1
                    continue
                else:
                    idx.append(i)

        return idx


    arr = []

    for i in range(len(files)):
        id = divide(files[i])
        if len(id) == 1:
            arr.append((files[i][:id[0]].upper(),  files[i][id[0]:], '', i))
        else:
            arr.append((files[i][:id[0]].upper(),  files[i]
                       [id[0]:id[1]], files[i][id[1]:].upper(), i))

    arr.sort(key=lambda x: int(x[1]))
    arr.sort(key=lambda x: x[0])
    answer = []
    for i in arr:
        answer.append(files[i[3]])

    return answer

