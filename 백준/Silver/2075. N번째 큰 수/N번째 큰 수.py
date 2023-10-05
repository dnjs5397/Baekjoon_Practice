import sys
import heapq
N = int(input())

arr = []
for _ in range(N):
    for i in list(map(int, sys.stdin.readline().split())):
        heapq.heappush(arr, i)

    while (len(arr) > N):
        heapq.heappop(arr)

print(arr[0])
