import sys

N = int(input())
arr = list(map(int, sys.stdin.readline().split(' ')))
Q = int(input())
for i in range(Q):
    tmp = list(map(int, input().split(' ')))
    if tmp[0] == 1:
        X = tmp[1]
        summary = 0
        prefix_sum = [0]
        for j in arr:
            summary += j%X
            prefix_sum.append(summary)
        print(prefix_sum[N])
    elif tmp[0] == 2:
        X = tmp[1]
        summary = 0
        prefix_sum = [0]
        for j in arr:
            summary += X%j
            prefix_sum.append(summary)
        print(prefix_sum[N])

    else:
        arr[tmp[1]-1] = tmp[2]