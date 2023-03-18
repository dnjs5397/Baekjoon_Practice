def factorial(num):
    N = 1
    while(num > 0):
        N *= num
        num -= 1
    return N

def solution(n):
    ans = 0
    length = n//2

    for i in range(0, length+1):
        if i == 0:
            ans += 1
            continue
        N = i + (n-(i*2))
        R = (n-(i*2))
        if R == 0:
            ans += 1
            continue
        ans += factorial(N) // (factorial(N-R) * factorial(R))


    return ans%1234567
