N = int(input())
arr = list(map(int, input().split(' ')))
if N == 1:
    print(1)
    exit(0)
value = [1] * N
for i in range(1, N):
    max_val = 0
    max_index = 0
    for j in range(0, i):
        if arr[j] < arr[i]:
            if value[j] > max_val:
                max_val = value[j]
                max_index = j
    if max_val != 0:
        value[i] += value[max_index]

print(max(value))