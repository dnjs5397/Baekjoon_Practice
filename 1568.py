N = int(input())
count = 0
sing = 1
while(N != 0):
    if (N < sing):
        sing = 1
    else:
        N -= sing
        sing += 1
        count += 1

print(count)
