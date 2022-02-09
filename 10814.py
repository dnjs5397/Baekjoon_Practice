N = int(input())

result = []

for i in range(N):
    data =  input().split(' ')
    result.append((int(data[0]), data[1]))
    
result.sort(key = lambda x : x[0])

for i in result:
    print(i[0], i[1])