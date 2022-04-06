import sys
result = 0
N = int(input())
arr = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split(' '))
    arr.append((a,b))

arr.sort(key = lambda x : (x[1], x[0]))
for i in range(N):
    if i == 0:
        result += (arr[i+1][0] - arr[i][0])
        continue
    if i == N-1:
        result += (arr[i][0] - arr[i-1][0])
        continue
    if arr[i][1] == arr[i-1][1]:
        val1 = arr[i][0] - arr[i-1][0]
    else:
        val1 = 9912341234
    if arr[i][1] == arr[i+1][1]:
        val2 = arr[i+1][0] - arr[i][0]
    else:
        val2 = 9912341234
    val = min(val1, val2)
    result += val
    
print(result)