N = int(input())
arr = list(map(int, input().split(' ')))
result = []
arr2 = list(set(arr))
for i in range(len(arr2)):
    result.append((i, arr2[i]))

for i in arr:
    a = 1