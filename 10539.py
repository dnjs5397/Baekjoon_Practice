N, arr = int(input()), list(map(int, input().split()))
result = []
result.append(arr[0])

for i in range(1, N):
    result.append(arr[i]*(i+1) - sum(result))

for i in range(N):
    print(result[i], end=' ')