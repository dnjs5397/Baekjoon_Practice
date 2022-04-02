import operator as op
from functools import reduce


def nCr(n, r):
    if n < 1 or r < 0 or n < r:
        raise ValueError
    r = min(r, n-r)
    numerator = reduce(op.mul, range(n, n-r, -1), 1)
    denominator = reduce(op.mul, range(1, r+1), 1)
    return numerator // denominator


N = int(input())
S = input()
W = []
H = []
E = []
for i in range(len(S)):
    if S[i] == 'W':
        W.append(i)
    elif S[i] == 'H':
        H.append(i)
    elif S[i] == 'E':
        E.append(i)
answer = 0
for i in W:
    for j in H:
        if j < i:
            continue
        for k in range(len(E)):
            if E[k] < j:
                continue
            length = len(E[k:])
            if length < 2:
                break
            else:    
                for q in range(2, length+1):
                    answer += (nCr(length, q) % 1000000007)
                break

print(answer%1000000007)