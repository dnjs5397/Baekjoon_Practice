N = int(input())
arr = list(map(int, input().split()))
max = max(arr)
min = min(arr)
result = max - min
print(result)