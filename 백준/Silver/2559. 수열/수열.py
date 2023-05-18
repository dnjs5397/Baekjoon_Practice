N,M = map(int, input().split())
arr = list(map(int, input().split()))
answer = []
idx = 0
cnt = 0
sum = 0
for i in range(len(arr)):
    if cnt < M:
        sum += arr[i]
        cnt += 1
    else:
        answer.append(sum)
        sum += arr[i]
        sum -= arr[idx]
        idx += 1
        
answer.append(sum)
print(max(answer))