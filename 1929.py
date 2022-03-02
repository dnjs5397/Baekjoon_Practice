import math

M, N = map(int, input().split(' '))
num = [True for i in range(N+1)]
for i in range(2, int(math.sqrt(N))+1):
    if num[i] == True:
        j = 2
        while(i*j <= N):
            num[i*j] = False
            j += 1

for i in range(M, N+1):
    if num[i] and i != 1:
        print(i)