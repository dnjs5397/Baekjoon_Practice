N = int(input())
list = []
for i in range(0,N):
    list.append(int(input()))
list.sort()
list.reverse()
for i in range(0,N):
    list[i] = list[i] * (i+1)

print(max(list))

