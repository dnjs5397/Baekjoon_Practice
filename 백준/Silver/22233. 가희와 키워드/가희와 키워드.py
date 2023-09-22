import sys

N, M = map(int, input().split())
d = dict()
for _ in range(N):
    t = sys.stdin.readline().rstrip()
    d[t] = 1
answer = len(d)
for _ in range(M):
    val = 0
    tmp = list(map(str, sys.stdin.readline().rstrip().split(',')))
    for tt in tmp:
        if tt in d:
            if d[tt] == 1:
                d[tt] = 0
                val += 1

    answer -= val
    print(answer)
