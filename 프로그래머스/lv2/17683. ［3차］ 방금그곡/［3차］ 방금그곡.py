def solution(m, mm):
    answer = []
    m = m.replace('C#', 'c')
    m = m.replace('D#', 'd')
    m = m.replace('F#', 'f')
    m = m.replace('G#', 'g')
    m = m.replace('A#', 'a')


    def time(st):
        return (int(st[:2])*60 + int(st[3:]))


    for i in range(len(mm)):
        t = mm[i].split(',')
        cnt = time(t[1])-time(t[0])
        t[3] = t[3].replace('C#', 'c')
        t[3] = t[3].replace('D#', 'd')
        t[3] = t[3].replace('F#', 'f')
        t[3] = t[3].replace('G#', 'g')
        t[3] = t[3].replace('A#', 'a')
        if cnt <= len(t[3]):
            w = t[3][:cnt]
        else:
            w = (t[3]*(cnt//len(t[3])+1))[:cnt]

        if m in w:
            answer.append([i, cnt, t[2]]) 

    if answer:
        answer.sort(key=lambda x: x[0])
        answer.sort(key=lambda x: x[1], reverse=True)
        return (answer[0][2])
    else:
        return "(None)"