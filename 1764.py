N, M = map(int, input().split(' '))
arr = set()
arr2  = set()
for i in range(N):
    arr.add(input())
for i in range(M):
    arr2.add(input())

tmp = set()
answer = set()
if (N > M):
    tmp = arr - arr2
    answer = arr - tmp
else:
    tmp = arr2 - arr
    answer = arr2 - tmp

answer = list(answer)
answer.sort()
print(len(answer))
for i in answer:
        print(i)