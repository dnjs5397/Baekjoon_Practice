N = int(input())
cost = list(map(int, input().split()))
pay = int(input())

if sum(cost) <= pay:
    print(max(cost))
    exit(0)

l = 0
r = sum(cost)


def cal(arr, m):
    t = 0
    for i in arr:
        if i <= m:
            t += i
        else:
            t += m

    return t


answer = -1
while (l <= r):
    mid = (l+r)//2

    val = cal(cost, mid)
    if val <= pay:
        l = mid + 1
        answer = max(answer, mid)
    else:
        r = mid - 1

print(answer)
