import sys

N,M = map(int, input().split())
arr = list(map(int, input().split()))
if len(arr) >= 2:
    for i in range(1, len(arr)):
        arr[i] += arr[i-1]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    if a == 1:
        print(arr[b-1])
    else:
        print(arr[b-1]-arr[a-2])