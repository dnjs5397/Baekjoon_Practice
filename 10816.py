N = int(input())
n = list(map(int, input().split(' ')))
M = int(input())
m = list(map(int, input().split(' ')))

result = []
dic= dict()

for i in n:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in m:
    if i in dic:
        result.append(dic[i])
    else:
        result.append(0)

for i in result:
    print(i, end = ' ')