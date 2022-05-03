N = int(input())

arr = [i+1 for i in range(N)]

tmp = []

while(len(arr) != 1):
    for i in range(len(arr)):
        if i%2:
            tmp.append(arr[i])
    arr = tmp
    tmp = []
print(arr[0])
