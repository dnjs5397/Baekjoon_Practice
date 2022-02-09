# 계수 정렬 알고리즘
import sys

N = int(sys.stdin.readline())

answer = [0 for i in range(10001)]

for i in range(N):
    tmp = int(sys.stdin.readline())
    answer[tmp] += 1
    
for i in range(len(answer)):
    for j in range(answer[i]):
        print(i)
