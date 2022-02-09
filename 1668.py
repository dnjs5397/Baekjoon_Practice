N = int(input())
left = 0
right = 0
tro = []
for i in range(N):
    tro.append(int(input()))

if (N == 1):
    print(1)
    print(1)
else:
    max = tro[0]
    left += 1
    for i in range(1, N):
        if (tro[i] > max):
            left += 1
            max = tro[i]
    
    max = tro[N-1]
    right += 1
    for i in range(N-2, -1, -1):
        if (tro[i] > max):
            right += 1
            max = tro[i]
            
    print(left)
    print(right)