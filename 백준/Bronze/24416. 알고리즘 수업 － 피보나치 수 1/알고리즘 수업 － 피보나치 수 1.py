def f1(n):
    global a
    if n==1 or n==2:
        return 1
    else:
        return (f1(n-1) + f1(n-2))
    
N = int(input())
print(f1(N), N-2)