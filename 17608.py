import sys

N = int(input())
arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline()))
cnt = 1
value = arr[N-1]
for i in range(N-1, -1, -1):
    if arr[i] > value:
        cnt += 1
        value = arr[i]

print(cnt)