brown = 18
yellow = 6
num = brown+yellow
answer = []
for i in range(1, num+1):
    if num % i == 0:
        if i >= num//i and (i-2)*(num//i-2) == yellow:
            answer.append(i)
            answer.append(num//i)
            break
            
print(answer)