S = list(input())

zero = S.count('0')
one = S.count('1')

zero = zero//2
one = one//2
idx = 0
while (one > 0):
    if S[idx] == '1':
        if one > 0:
            S[idx] = 'X'
            one -= 1

    idx += 1

idx = len(S)-1
while (zero > 0):
    if S[idx] == '0':
        if zero > 0:
            S[idx] = 'X'
            zero -= 1

    idx -= 1

answer = ''
for s in S:
    if s != 'X':
        answer += s

print(answer)
