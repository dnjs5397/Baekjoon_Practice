N = int(input())
arr = []
for i in range(N):
    arr.append((input(), i))
data = set()
cnt = 0
for i in range(N-1):
    for j in range(i+1, N):
        if arr[i][0][0] == arr[j][0][0]:
            c = 0
            for k in range(min(len(arr[i][0]), len(arr[j][0]))):
                if arr[i][0][k] == arr[j][0][k]:
                    c += 1
                else:
                    break
            if cnt < c:
                cnt = c
                data.add((i, c))
                data.add((j, c))

answer = []
for i in data:
    if i[1] == cnt:
        answer.append(arr[i[0]])
answer.sort(key=lambda x: x[1])
for i in answer:
    print(i[0])
