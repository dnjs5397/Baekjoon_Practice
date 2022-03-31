N = int(input())
box = list(map(int, input().split(' ')))
boxes = [1 for _ in range(N)]
if N == 1:
    print(1)
    exit(0)

for i in range(1, N):
    idx = i-1
    while (idx > -1):
        if box[idx] < box[i]:
             boxes[i] += boxes[idx]
             break
        idx -= 1

print(max(boxes))