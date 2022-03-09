N = int(input())
tmp = list(map(int, input().split(' ')))
arr = []
result = [0] * N
for i in range(N):
    arr.append((i, tmp[i]))
arr.sort(key = lambda x : x[1])

for i in range(1, N):
    small = []
    value = arr[i][1]
    index = i
    while(index >= 1):
        index -= 1
        if arr[index][1] == value:
            pass
        else:
            small.append(arr[index][1])
    small = list(set(small))
    result[arr[i][0]] = len(small)

print(result)
        