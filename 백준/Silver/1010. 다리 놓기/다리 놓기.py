def factorial(n):
    num = 1
    for i in range(2, n+1):
        num *= i
    return num

T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    if N == M:
        print(1)
        continue
    ans = factorial(M) // (factorial(N) * factorial(M-N))
    print(ans)