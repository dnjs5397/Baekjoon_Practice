T = int(input())
for i in range(T):
    count = 0
    N = int(input())
    child = list(map(int, input().split(' ')))
    for i in range(N): # 아이들의 사탕 개수가 홀수이면 짝수로 맞춰줌
        if (child[i]%2 != 0): 
            child[i] += 1
    while (child.count(child[0]) != N): # 루프를 돌면서 아이들의 사탕 개수가 모두 같아질때까지 반복
        # 배열의 원소가 같은지 체크하는 방법 2)
        # len(set(child) == 1)
        candy = []
        for i in range(N): # 사탕 개수 반으로 나눔
            candy.append(child[i]//2)  
            child[i] //= 2
        for i in range(N): # 사탕 전달
            if (i == N-1):
                child[0] += candy[i]
            else:
                child[i+1] += candy[i]
        for i in range(N): # 아이들의 사탕 개수가 홀수이면 짝수로 맞춰줌
            if (child[i]%2 != 0):
                child[i] += 1
        count += 1
    print(count) # 출력