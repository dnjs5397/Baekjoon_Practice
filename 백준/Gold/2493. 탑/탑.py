N = int(input())
arr = list(map(int, input().split()))
answer = [0] * N
stack = []
for i in range(N):
    if stack == []:
        answer[i] = 0
        stack.append((arr[i], i+1))
    else:
        if stack[-1][0] > arr[i]:
            answer[i] = stack[-1][1]
            stack.append((arr[i], i+1))
        else:
            while (stack):
                stack.pop()
                if stack == []:
                    answer[i] = 0
                    stack.append((arr[i], i+1))
                    break

                if stack[-1][0] > arr[i]:
                    answer[i] = stack[-1][1]
                    stack.append((arr[i], i+1))
                    break


print(*answer)
