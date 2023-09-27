T = int(input())
for _ in range(T):
    n, k, t, m = map(int, input().split())
    submit = [0] * n
    time = [0] * n

    score = [[0 for i in range(k)] for j in range(n)]
    for q in range(m):
        x, y, num = map(int, input().split())
        score[x-1][y-1] = max(score[x-1][y-1], num)
        submit[x-1] += 1
        time[x-1] = q

    answer = []
    for i in range(n):
        tmp = [i+1, sum(score[i]), submit[i], time[i]]
        answer.append(tmp)

    answer.sort(key=lambda x: x[3])
    answer.sort(key=lambda x: x[2])
    answer.sort(key=lambda x: x[1], reverse=True)

    for i in range(len(answer)):
        if answer[i][0] == t:
            print(i+1)
            break
