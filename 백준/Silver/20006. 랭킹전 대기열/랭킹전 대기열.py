import sys

p, m = map(int, sys.stdin.readline().split())
arr = []
for _ in range(p):
    l, n = map(str, sys.stdin.readline().split())
    if arr == []:
        arr.append([])
        arr[0].append((int(l),n))
    else:
        for ar in arr:
            if len(ar) < m:
                if ar[0][0]-10 <= int(l) <= ar[0][0]+10:
                    ar.append((int(l),n))
                    break

        else:
            arr.append([])
            arr[-1].append((int(l),n))
        
for ar in arr:
    if len(ar) == m:
        print("Started!")
        for a in sorted(ar, key=lambda x:x[1]):
            print(a[0], a[1])
    else:
        print("Waiting!")
        for a in sorted(ar, key=lambda x:x[1]):
            print(a[0], a[1])