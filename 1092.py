N = int(input())
crain = list(map(int, input().split(' ')))
crain.sort(reverse=True)
M = int(input())
box = list(map(int, input().split(' ')))
box.sort(reverse=True)
count = 0
while(len(box)!=0):
    count += 1
    for i in range(N):
        cnt = 0
        while(1):
            if (crain[i] >= box[cnt]):
                break
            elif box[cnt] > max(crain):
                print(-1)
                exit(0)
            else:
                cnt += 1
        box.pop(cnt)
        if (len(box) == 0):
            print(count)
            exit(0)

print(count)