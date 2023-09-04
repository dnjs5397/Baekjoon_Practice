N = int(input())
arr = []
dp = [0] * N
for i in range(N):
    arr.append(int(input()))

dp[0] = 1
for i in range(1, N):
    cnt = 0
    for j in range(i):
        if arr[j] < arr[i]:
            cnt = max(cnt, dp[j])
    dp[i] = cnt + 1

print(N-max(dp))
