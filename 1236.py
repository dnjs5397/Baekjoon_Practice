N, M = map(int , input().split(' '))
col_count = 0
row_count = 0
arr = []
for i in range(N):
    arr.append(input())
    if 'X' not in arr[i]:
        row_count += 1
    
for i in range(M):
    count = 0
    for j in range(N):
        if arr[j][i] == 'X':
            count += 1
    if (count == 0):
        col_count += 1

print(max(row_count, col_count))