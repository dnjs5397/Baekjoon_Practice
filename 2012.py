N = int(input())
result = 0
score = []
for i in range(N):
    score.append(int(input()))
score.sort()
for i in range(N):
    result += abs(score[i] - (i+1))
print(result)