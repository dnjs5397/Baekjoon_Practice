N = int(input())
distance = list(map(int, input().split()))
arr = list(map(int, input().split()))
distance.insert(0, 0)

answer = [0] * N

for i in range(1, N):
    answer[i] = arr[0] * distance[i] + answer[i-1]

for i in range(2, N):
    val = answer[i-1]
    for j in range(i, N):
        val += arr[i-1]*distance[j]
        if val <= answer[j]:
            answer[j] = val
        else:
            break

print(answer[-1])
