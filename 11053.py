N = int(input())
arr = list(map(int, input().split(' ')))
result = 1
for i in range(N-1):
    num = arr[i]
    tmp_result = 1
    for j in range(i+1, N):
        if i == N-2:
            if arr[i] < arr[-1]:
                tmp_result = 2
                break
            else:
                tmp_result = 1
                break
        if arr[j] > num:
            num = arr[j]
            tmp_result += 1
    result = max(result, tmp_result)

print(result)