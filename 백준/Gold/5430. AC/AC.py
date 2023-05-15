import collections

for _ in range(int(input())):
    what = True
    br = True
    command = input()
    length = int(input())
    a = input()
    if a == '[]':
        if 'D' in command:
            print('error')
            continue
        else:
            print('[]')
            continue    
    a = list(a)
    a.pop(0)
    a.pop(-1)
    a = ''.join(a)
    b = a.split(sep=',')
    b = collections.deque(b)
    for i in command:
        if i == 'D':
            if len(b) == 0:
                print('error')
                br = False
                break
            if what==True:
                b.popleft()
            else:
                b.pop()
        if i == 'R':
            what = not what
    if br:
        if what:
            answer = []
            for j in range(len(b)):
                answer.append(int(b[j]))
            an = ''
            answer = str(answer)
            for i in answer:
                if i != ' ':
                    an += i
            print(an)

        else:
            answer = []
            for j in range(len(b)-1, -1, -1):
                answer.append(int(b[j]))
            an = ''
            answer = str(answer)
            for i in answer:
                if i != ' ':
                    an += i
            print(an)