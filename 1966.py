import queue

n = int(input())

for i in range(n):
    n,m = map(int, input().split(' '))
    queue = list(map(int, input().split(' ')))
    queue = [(i, index) for index, i in enumerate(queue)]

    count = 0
    while True:
        if queue[0][0] == max(queue, key= lambda x : x[0])[0]:
            count += 1 
            if queue[0][1] == m:
                print(count)
                break
