N = int(input())

sum = 0
cnt = 0
for i in range(1, N+1):
    cnt += 1
    sum += i
    if sum > N:
        print(cnt-1)
        exit(0)
    elif sum == N:
        print(cnt)
        exit(0)
