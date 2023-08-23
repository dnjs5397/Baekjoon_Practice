n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
answer = []


def dfs(v):
    if len(answer) == m:
        for i in answer:
            print(arr[i], end=' ')
        print()
        return

    for i in range(v, n):
        answer.append(i)
        dfs(i)
        answer.pop()


dfs(0)