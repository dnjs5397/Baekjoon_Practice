N = int(input())
N = str(N)
result = []
for i in range(len(N)):
    result.append(N[i])
result.sort(reverse=True)
print(''.join(result))