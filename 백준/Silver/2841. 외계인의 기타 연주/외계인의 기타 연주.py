import sys
N, P = map(int, input().split())
ar = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    ar.append((a, b))

arr = [[] for i in range(N+1)]
finger = 0
for m in ar:
    if arr[m[0]] == []:
        finger += 1
        arr[m[0]].append(m[1])

    else:
        if arr[m[0]][-1] < m[1]:
            finger += 1
            arr[m[0]].append(m[1])
        elif arr[m[0]][-1] == m[1]:
            continue
        else:
            while (arr[m[0]][-1] > m[1]):
                finger += 1
                arr[m[0]].pop()
                if arr[m[0]] == []:
                    break

            if arr[m[0]] == []:
                finger += 1
                arr[m[0]].append(m[1])
                continue

            if arr[m[0]][-1] == m[1]:
                continue
            else:
                arr[m[0]].append(m[1])
                finger += 1

print(finger)