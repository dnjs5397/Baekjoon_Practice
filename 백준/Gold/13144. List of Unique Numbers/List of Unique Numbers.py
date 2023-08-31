N = int(input())
arr = list(map(int, input().split()))
check = [0] * (N+1)
check[0] = 1
left = 0
right = 0

answer = 0

while(left < N and right < N):
    if not check[arr[right]]:
        check[arr[right]] = 1
        right += 1
        answer += right-left
        
    else:
        check[arr[left]] = 0
        left += 1

print(answer)