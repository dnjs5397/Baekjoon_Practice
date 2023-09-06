st = list(input())
cnt = 1
num = [1] * 10

for s in st:
    if num[int(s)] >= 1:
        num[int(s)] -= 1
    else:
        if int(s) == 6:
            if num[9] >= 1: 
                num[9] -= 1
                continue
        if int(s) == 9:
            if num[6] >= 1: 
                num[6] -= 1
                continue

        cnt += 1
        for i in range(10):
            num[i] += 1
        num[int(s)] -= 1

print(cnt)