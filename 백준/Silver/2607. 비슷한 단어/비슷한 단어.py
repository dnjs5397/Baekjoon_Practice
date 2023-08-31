N = int(input())
word = list(input())
word.sort()
arr = []
for _ in range(N-1):
    arr.append(list(input()))

for i in range(N-1):
    arr[i].sort()
    
alpha = [0] * 26
for i in word:
    alpha[ord(i)-65] += 1

answer = 0
for ww in arr:
    if word == ww:
        answer += 1
        continue
    al = [0] * 26
    if len(word) == len(ww):
        for w in ww:
            al[ord(w)-65] += 1
        cnt =0
        for i in range(26):
            if al[i] != alpha[i]:
                cnt += abs(al[i]-alpha[i])
            if cnt > 2:
                break
        if cnt <= 2:
            answer += 1
        continue
    
    if abs(len(word)-len(ww)) == 1:
        for w in ww:
            al[ord(w)-65] += 1
        cnt =0
        for i in range(26):
            if al[i] != alpha[i]:
                cnt += abs(al[i]-alpha[i])
            if cnt >= 2:
                break
        if cnt < 2:
            answer += 1
        continue

print(answer)