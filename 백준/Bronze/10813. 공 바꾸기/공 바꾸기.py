N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
for _ in range(M):
    i,j = map(int, input().split())
    tmp = arr[i-1]
    arr[i-1] = arr[j-1]
    arr[j-1] = tmp
    

for i in arr:
    print(i, end=' ')