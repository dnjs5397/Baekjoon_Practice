import sys


N, M = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

for _ in range(M):
    a,b = map(int, sys.stdin.readline().split(' '))
    print(sum(arr[a-1:b]))