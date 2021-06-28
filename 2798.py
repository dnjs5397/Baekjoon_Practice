# 블랙잭, 탐색 문제
# 파이썬은 1초에 2천만까지의 연산 가능
N, M = input().split(' ')
N = int(N)
M = int(M)

card = list(map(int, input().split(' ')))

max = 0
sum = 0

for i in range(0, N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum = card[i] + card[j] + card[k]
            if (sum >= max and sum <= 21):
                max = sum

print(max)