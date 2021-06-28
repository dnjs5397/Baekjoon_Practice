# 블랙잭, 탐색 문제

N, M = input().split(' ')
N = int(N)
M = int(M)

card = list(map(int, input().split(' ')))

max = 0
sum = 0

for i in range(0, N):
    for j in range(1, N):
        for k in range(2, N):
            sum = card[i] + card[j] + card[k]
            if (sum >= max and sum <= 21):
                max = sum

print(max)