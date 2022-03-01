# DP
N = int(input())
if N <= 2:
    print(N)
else:
    answer = [0 for i in range(N+1)]
    answer[1] = 1
    answer[2] = 2
    for i in range(3, N+1):
        answer[i] = answer[i-1] + answer[i-2]
    print(answer[i]%10007)