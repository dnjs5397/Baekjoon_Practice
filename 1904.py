arr = [1,2]

N = int(input())

if N <= 2:
    print(arr[N-1])
    exit(0)

for i in range(2, N):
    arr.append((arr[i-1]+arr[i-2])%15746)

print(arr[N-1])