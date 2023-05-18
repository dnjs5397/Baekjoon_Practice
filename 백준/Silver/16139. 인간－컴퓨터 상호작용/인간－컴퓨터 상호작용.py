st = input()
arr = [[0 for i in range(len(st))] for j in range(26)]
arr[ord(st[0])-97][0] = 1
for i in range(1, len(st)):
    for j in range(26):
        arr[j][i] += arr[j][i-1]
    arr[ord(st[i])-97][i] += 1

q = int(input())
for i in range(q):
    a, b, c = map(str, input().split())
    if int(b) == 0:
        print(arr[ord(a)-97][int(c)])
    else:
        print(arr[ord(a)-97][int(c)] - arr[ord(a)-97][int(b)-1])