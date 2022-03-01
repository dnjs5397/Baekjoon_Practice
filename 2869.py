A, B, V = map(int, input().split(' '))
if (A==V):
    print(1)
    exit(0)
day = A-B
V -= A
result = 1
if (V <= day):
    print(result+1)
    exit(0)
if V%day == 0:
    print(result+V//day)
else:
    print(result+1+V//day)