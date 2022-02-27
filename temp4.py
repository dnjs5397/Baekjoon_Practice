N = int(input())
count = 0

S = input()
cnt = 1
for i in range(N-1):
    if S[i] == S[i+1]:
        cnt += 1
    else:
        if cnt % 3 == 0:
            count += 1
        cnt = 1
    if i == N-2:
        if cnt % 3 == 0:
            count += 1
print(count)