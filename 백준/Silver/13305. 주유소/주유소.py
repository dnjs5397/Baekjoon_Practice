N = int(input())
distance = list(map(int, input().split()))
arr = list(map(int, input().split()))

answer = 0
cnt = arr[0]

for i in range(N-1):
    if arr[i] < cnt:
        cnt = arr[i]
    answer += cnt * distance[i]


print(answer)
