def solution(a):
    x = a[0]
    i = 0
    cnt = 0
    O = 0
    X = 0
    if len(a) == 1:
        return 1
    else:
        while(i < len(a)):
            if a[i] == x:
                O += 1
            else:
                X += 1

            if X == O:
                X = 0
                O = 0
                cnt += 1
                i += 1
                if i == len(a):
                    return cnt
                else:
                    x = a[i]
            else:
                i += 1
        return cnt+1