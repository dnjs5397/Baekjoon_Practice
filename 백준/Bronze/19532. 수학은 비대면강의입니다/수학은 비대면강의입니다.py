arr = [i for i in range(1, 1000)]
arr2 = [i*-1 for i in range(1, 1000)]
answer = arr + [0] + arr2
a, b, c, d, e,f = map(int, input().split())
for i in range(1999):
    for j in range(1999):
        if (a*answer[i] + b*answer[j] == c and 
            d*answer[i] + e*answer[j] == f):
            print(answer[i], answer[j], end=' ')
            exit(0)