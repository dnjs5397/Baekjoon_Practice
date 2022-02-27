N = int(input())
crain = list(map(int, input().split(' ')))
crain.sort(reverse=True)
M = int(input())
box = list(map(int, input().split(' ')))
box.sort(reverse=True)
if crain[0] < box[0]: # 가장 무거운 박스가 크레인의 무게 제한보다 높다면 -1 리턴 후 종료
    print('-1')
    exit(0)
count = 0 # 분 카운트
while(len(box)!=0):
    count += 1 # 1분 증가했다고 판정
    for i in range(N): # 크레인 개수만큼 돌면서
        cnt = 0
        while(1): # 해당 크레인이 들 수 있는 박스를 찾기 위한 반복
            if (crain[i] >= box[cnt]):
                break
            else:
                cnt += 1
            if (cnt == len(box)): # 해당 크레인이 들 수 있는 박스가 없다면 다음 크레인으로 넘어감
                break
        if (cnt == len(box)): # 해당 크레인이 들 수 있는 박스가 없다면 다음 크레인으로 넘어감
            continue
        box.pop(cnt)
        if (len(box) == 0):
            print(count)
            exit(0)

print(count)