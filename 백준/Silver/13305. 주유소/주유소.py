N = int(input())
distance = list(map(int, input().split()))
arr = list(map(int, input().split()))
distance.insert(0, 0)

answer = [0] * N

answer[1] = arr[0] * distance[1]

for i in range(2, N):
    answer[i] = min(answer[i-1]+arr[i-1]*distance[i],
                    answer[i-1]+arr[i-2]*distance[i])

print(answer[N-1])
