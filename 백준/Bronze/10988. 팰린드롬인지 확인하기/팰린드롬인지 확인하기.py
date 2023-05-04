a = input()
arr = []
arr2 = []
for i in a:
    arr.append(i)
    arr2.append(i)

arr2.reverse()

if arr == arr2:
    print(1)
else:
    print(0)