top = [[], [], [], []]

for i in range(4):
    a = input()
    for j in a:
        top[i].append(int(j))


def turn(num, dir):
    if dir == 1:
        top[num].insert(0, top[num].pop())
    else:
        top[num].append(top[num].pop(0))


def direction(num, dir):
    left, right = num - 1, num + 1
    if 0 <= left <= 3:
        if top[num][-2] != top[left][2] and ch[left] == 0:
            dd.append((left, dir*-1))
            ch[left] = 1
            direction(left, dir*-1)

    if 0 <= right <= 3:
        if top[num][2] != top[right][-2] and ch[right] == 0:
            dd.append((right, dir*-1))
            ch[right] = 1
            direction(right, dir*-1)


t = int(input())

for _ in range(t):
    dd = []
    ch = [0] * 4
    n, d = map(int, input().split())
    dd.append((n-1, d))
    ch[n-1] = 1
    direction(n-1, d)

    for i in dd:
        turn(i[0], i[1])

answer = 0
for i in range(4):
    if top[i][0] == 1:
        if i == 0:
            answer += 1
        elif i == 1:
            answer += 2
        elif i == 2:
            answer += 4
        elif i == 3:
            answer += 8
            
print(answer)
