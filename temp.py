food_times = [4,2,3,6,7,1,5,8]
k=27

foods = []
n = len(food_times) # 음식의 개수
for i in range(n):
    foods.append((food_times[i], i+1))
print(foods)
foods.sort() # 음식 시간 값으로 정렬

pretime = 0
for i, food in enumerate(foods):
    print(food,food[0],food[1])
    diff = food[0] - pretime
    if diff != 0:
        spend = diff * n
        if spend <= k:
            k -= spend
            pretime = food[0]
        else:
            k %= n
            sublist = sorted(foods[i:], key = lambda x : x[1])
            #print(sublist[k][1])
    n -= 1
#print(-1)