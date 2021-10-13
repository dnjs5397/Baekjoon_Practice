N, M = map(int, input().split())
A, B = map(str, input().split())
arr = []
result = []
if (N < M):
    for i in range(N):
        arr.append(A[i])
        arr.append(B[i])
    for i in range(N, M):
        arr.append(B[i])
elif (N > M):
    for i in range(M):
        arr.append(A[i])
        arr.append(B[i])
    for i in range(M, N):
        arr.append(A[i])
else:
    for i in range(N):
        arr.append(A[i])
        arr.append(B[i])

for i in range(len(arr)):
    if (arr[i] == 'C' or arr[i] == 'G' or arr[i] == 'I' or arr[i] == 'J' 
        or arr[i] == 'L' or arr[i] == 'O' or arr[i] == 'S' or arr[i] == 'U'
        or arr[i] == 'V' or arr[i] == 'W' or arr[i] == 'Z'):
        result.append(1)
    elif (arr[i] == 'B' or arr[i] == 'D' or arr[i] == 'N' or arr[i] == 'P'
          or arr[i] == 'Q' or arr[i] == 'R' or arr[i] == 'T' or arr[i] == 'X' or arr[i] == 'Y'):
          result.append(2)
    elif (arr[i] == 'A' or arr[i] == 'F' or arr[i] == 'H' or arr[i] == 'K' or arr[i] == 'M'):
        result.append(3)
    else:
        result.append(4)

count = len(result)
while(count > 2):
    for i in range(count-1):
        result[i] = (result[i] + result[i+1]) % 10
    count -= 1

if (result[0] == 0):
    print(result[1], end='')
    print('%')
else:
    for i in range(2):
        print(result[i], end='')
    print('%')