land = [[1,2,3,5]]
if len(land) == 1:
    print(max(land[0]))
    exit(0)
for i in range(1, len(land)):
    for j in range(4):
        num = land[i][j]
        score = 0
        for k in range(4):
            if k != j:
                if num + land[i-1][k] > score:
                    score = num + land[i-1][k]
        land[i][j] = score

print(max(land[len(land)-1]))