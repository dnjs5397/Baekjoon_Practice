N = int(input())
person = []
for _ in range(N):
    a, b = map(int, input().split(' '))
    person.append((a, b))
grade = []
for i in range(N):
    cnt = 0
    kg = person[i][0]
    cm = person[i][1]
    for j in range(N):
        if i != j:
            if person[j][0] > kg and person[j][1] > cm:
                cnt += 1
    grade.append(cnt+1)

for i in grade:
    print(i, end=' ')