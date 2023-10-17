st = input()

s = ''
cnt = 1

for i in range(len(st)):
    if i > 0:
        if st[i] == 'c':
            if s == st[i]:
                cnt *= 25
            else:
                cnt *= 26
                s = st[i]
        else:
            if s == st[i]:
                cnt *= 9
            else:
                cnt *= 10
                s = st[i]
    else:
        if st[i] == 'c':
            cnt *= 26
            s = st[i]
        else:
            cnt *= 10
            s = st[i]

print(cnt)
