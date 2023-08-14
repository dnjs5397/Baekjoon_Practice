import sys
N, M = map(int, input().split())

words = []
t = dict()
for i in range(N):
    tmp = input()
    if len(tmp) >= M:
        words.append(tmp)
        if tmp in t:
            t[tmp] += 1
        else:
            t[tmp] = 1

words.sort()
words.sort(key=lambda x: len(x), reverse=True)
words.sort(key=lambda x: t[x], reverse=True)

tt = dict()

for i in words:
    if i in tt:
        continue
    else:
        tt[i] = 1
        print(i)
