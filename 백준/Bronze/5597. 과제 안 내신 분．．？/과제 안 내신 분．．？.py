arr = dict()
for i in range(28):
    arr[int(input())] = 1

for i in range(1, 31):
    if i not in arr:
        print(i)
