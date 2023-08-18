def solution(n, t, m, p):
    w = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    def binn(num, nn):
        st = ''

        while (num >= nn):
            if num % nn >= 10:
                st = w[num % nn] + st
            else:
                st = str(num % nn) + st
            num = num // nn
        if (num % n) >= 10:
            st = w[num % n] + st
        else:
            st = str(num) + st
        return st

    ans = ''
    cnt = 0
    while (1):
        ans += binn(cnt, n)
        if len(ans) >= t*m:
            break
        cnt += 1

    answer = ''
    c = p-1
    while (len(answer) < t):
        answer += ans[c]
        c += m
    return answer