import sys
sys.setrecursionlimit(10**4)
N, K = map(int, input().split())

dp = [214700000] * 100001

dp[N] = 0

stack = []
stack.append(N)
while (stack):
    idx = stack.pop(0)

    if idx*2 <= 100000:
        if dp[idx] < dp[idx*2]:
            dp[idx*2] = dp[idx]
            stack.append(idx*2)

    if idx-1 >= 0:
        if dp[idx] < dp[idx-1]:
            dp[idx-1] = dp[idx]+1
            stack.append(idx-1)

    if idx+1 <= 100000:
        if dp[idx] < dp[idx+1]:
            dp[idx+1] = dp[idx]+1
            stack.append(idx+1)


print(dp[K])
