n = int(input())
count = 1
stack = list()
result = list()
for i in range (0,n):
    data = int(input())
    while count <= data:
        stack.append(count)
        count += 1
        result.append('+')
    
    if (stack[-1] == data):
        stack.pop()
        result.append('-')
    else:
        print('NO')
        exit(0)
