st = list(input())
what = list(input())
stack = []
for i in range(len(st)):
    stack.append(st[i])
    if len(stack) >= len(what):
        if stack[(-1)*len(what):] == what:
            cnt = len(what)
            while (cnt > 0):
                stack.pop()
                cnt -= 1

if stack:
    print(''.join(stack))
else:
    print('FRULA')
