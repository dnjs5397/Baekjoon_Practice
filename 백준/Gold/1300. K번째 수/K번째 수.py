N = int(input())
K = int(input())
arr = []

    
left = 1
right = K
while(left<=right):
    mid = (left+right)//2
    
    cnt = 0
    for i in range(1, N+1):
        cnt += min(mid//i, N)
    
    if cnt>= K:
        answer = mid
        right = mid -1
    else:
        left = mid + 1

print(answer)
