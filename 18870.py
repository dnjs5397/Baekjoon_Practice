from os import sep


N = int(input())
arr = list(map(int, input().split(' ')))
result = [0] * N
arr2 = list(set(arr))
arr2.sort()
dic = {}
for i in range(len(arr2)):
    dic[arr2[i]] = i
for i in range(N):
    result[i] = dic[arr[i]]

for i in result:
    print(i, end=' ')