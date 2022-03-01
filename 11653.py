# 소인수분해
N = int(input())
if N == 1:
    exit(0)
num = 2
answer = []
while(N != 1):
    if N % num == 0:
        answer.append(num)
        N /= num
    else:
        num += 1

for i in answer:
    print(i)