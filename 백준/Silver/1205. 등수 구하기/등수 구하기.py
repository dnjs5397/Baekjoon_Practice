N, score, P = map(int, input().split())

rank = []
idx = -1
if N > 0:
    s = list(map(int, input().split()))
else:
    print(1)
    exit(0)

for i in s:
    if len(rank) < P:
        rank.append(i)


for i in range(len(rank)):
    if score > rank[i]:
        rank.insert(i, score)
        idx = i
        if len(rank) >= P:
            rank.pop()

if idx == -1:
    if len(rank) < P:
        rank.append(score)
        idx = len(rank)-1

        if rank.count(score) > 1:
            print(idx+1-(rank.count(score)-1))
        else:
            print(idx+1)

    else:
        print(idx)
else:
    if rank.count(score) > 1:
        print(idx+1-(rank.count(score)-1))
    else:
        print(idx+1)
