def solution(a, b, n):
    answer = 0
    while(n >= a):
        getCoke = (n // a) * b
        n -= (n // a) * a
        n += getCoke
        answer += getCoke
    return answer