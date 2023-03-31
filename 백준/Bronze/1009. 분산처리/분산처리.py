import sys

T = int(input())

for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    num = 1
    if a % 10 == 0:
        print(10)
    else:
        while(b>0):
            num *= a
            num %= 10
            b -= 1
        print(num)