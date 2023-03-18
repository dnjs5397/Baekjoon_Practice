# def factorial(num):
#     N = 1
#     while(num > 0):
#         N *= num
#         num -= 1
#     return N

# def solution(n):
#     ans = 0
#     length = n//2

#     for i in range(0, length+1):
#         if i == 0:
#             ans += 1
#             continue
#         N = i + (n-(i*2))
#         R = (n-(i*2))
#         if R == 0:
#             ans += 1
#             continue
#         ans += factorial(N) // (factorial(N-R) * factorial(R))


#     return ans%1234567

# DP 유형의 대표 문제 -> 팩토리얼로도 풀 수 있지만 효율성을 위해 DP를 이해할 것
def solution(n):
    arr = [1] * 2 + [0] * n
    
    for i in range(2, n+1):
        arr[i] = arr[i-1] + arr[i-2]
    
    return arr[n]%1234567

