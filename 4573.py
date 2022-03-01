arr = set(range(1,10001))
result = set()

for i in range(1,10001):
    for j in str(i):
        i += int(j)
    result.add(i)

arr = arr-result
arr = list(arr)
arr.sort()
for i in arr:
    print(i)