N, K = map(int, input().split())
arr = list(input())
answer = 0
for i in range(N):
    if arr[i] == 'P':
        idx = -1
        for j in range(i-1, i-1-K, -1):
            if j < 0:
                break
            if arr[j] == 'H':
                idx = j

        if idx == -1:
            for j in range(i+1, i+1+K):
                if j >= N:
                    break
                if arr[j] == 'H':
                    idx = j
                    break

        if idx != -1:
            arr[idx] = 'X'
            answer += 1
print(answer)
