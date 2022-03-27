N, C = map(int, input().split(' '))
house = []
answer = 0
for i in range(N):
    house.append(int(input()))
houses = sorted(house)

left = house[1] - house[0]
right = house[-1] - house[0]
while left <= right:
    mid = (left+right)//2
    count = 1
    value = house[0]
    for i in range(1, len(house)):
        if house[i] >= value+mid:
            count += 1
            value = house[i]
    if count >= C:
        left = mid + 1
        answer = mid
    else:
        right = mid - 1

print(answer)