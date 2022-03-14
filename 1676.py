def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)
count = 0
N = int(input())
s = str(factorial(N))
index = len(s)-1
while(index >= 0):
    if s[index] != '0':
        print(count)
        exit(0)
    else:
        count += 1
        index -= 1