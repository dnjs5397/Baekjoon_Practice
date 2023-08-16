import collections

N = int(input())
arr = list(map(int, input().split()))
ar = collections.deque()

for i in range(N-1, -1, -1):
    if len(ar) <= arr[i]:
        ar.append(i+1)
    else:
        ar.insert(arr[i], i+1)

print(*list(ar))
