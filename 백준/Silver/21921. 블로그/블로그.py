N, X = map(int, input().split())
visit = list(map(int, input().split()))
answer = 0
cnt = 0
dp = [0] * N
dp[0] = visit[0]
for i in range(1, N):
    dp[i] = dp[i-1] + visit[i]

answer = [0] * N
answer[X-1] = dp[X-1]
for i in range(X, N):
    answer[i] = dp[i] - dp[i-X]

if max(answer) == 0:
    print('SAD')
else:
    print(max(answer))
    print(answer.count(max(answer)))
