T = int(input())

for _ in range(T):
    answerA = 21470000
    answerB = 0
    alpha = [0] * 26
    st = input()
    cnt = int(input())

    for s in st:
        alpha[ord(s)-97] += 1

    al = []
    for i in range(len(alpha)):
        if alpha[i] >= cnt:
            al.append(chr(i+97))

    if al == []:
        print(-1)
        continue

    for a in al:
        idx = []
        for i in range(len(st)):
            if st[i] == a:
                idx.append(i)

        for i in range(len(idx)-cnt+1):
            tmp = idx[i:i+cnt]
            answerA = min(answerA, tmp[-1]-tmp[0]+1)
            answerB = max(answerB, tmp[-1]-tmp[0]+1)

    print(answerA, answerB)
