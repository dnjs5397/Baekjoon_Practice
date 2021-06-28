# 블랙잭, 탐색 문제
# 파이썬은 1초에 2천만까지의 연산 가능
N, M = map(int, input().split(' '))
card = list(map(int, input().split(' ')))

max_value = 0
result = 0

for i in range(0, N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum = card[i] + card[j] + card[k]
            if (sum <= M and max_value <= sum):
                max_value = sum

print(max_value)