import sys

N = int(input())
arr = set()
for _ in range(N):
    name, state = sys.stdin.readline().strip().split(' ')
    if state == 'enter':
        arr.add(name)
    else:
        arr.remove(name)

answer = list(arr)
answer.sort(reverse=True)
for i in answer:
    print(i)