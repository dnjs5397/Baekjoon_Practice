# DP
N = int(input())
stair = []
for _ in range(N):
    stair.append(int(input()))
if N<=2:
    print(sum(stair))
    exit(0)
s1 = [stair[0], stair[0] + stair[1]]
s2 = [0, stair[1]]
for i in range(2, N):
    s1.append(s2[i-1]+stair[i])
    s2.append(max(s1[i-2], s2[i-2]) + stair[i])

print(max(s1[N-1], s2[N-1]))
