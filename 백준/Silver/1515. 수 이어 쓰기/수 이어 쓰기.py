N = list(input())

num = 1

while(len(N)>0):
    length = len(str(num))

    for n in str(num):
        if n == N[0]:
            N.pop(0)
        if len(N) == 0:
            break

    num += 1

print(num-1)