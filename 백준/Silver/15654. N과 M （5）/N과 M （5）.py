n, m = map(int, input().split())
arr = list(map(int, input().split()))
ch = [0] * n
arr.sort()
answer = []


def dfs(v):
    if v == m:
        for i in answer:
            print(arr[i], end=' ')
        print()
        return

    for i in range(n):
        if i not in answer:
            answer.append(i)
            dfs(v+1)
            answer.pop()


dfs(0)
