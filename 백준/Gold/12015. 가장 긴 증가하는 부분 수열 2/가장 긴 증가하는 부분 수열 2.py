import bisect

N = int(input())
arr = list(map(int, input().split()))

answer = [arr[0]]

for i in range(1, N):
    if answer[-1] < arr[i]:
        answer.append(arr[i])
    else:
        idx = bisect.bisect_left(answer, arr[i])
        answer[idx] = arr[i]

print(len(answer))
