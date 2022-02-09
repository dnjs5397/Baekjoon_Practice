N = int(input())
list1 = list(map(int, input().split()))
list1 = set(list1)
M = int(input())
list2 = list(map(int, input().split()))

answer = [0 for i in range(M)]

for i in range(len(list2)):
    if (list2[i] in list1):
        answer[i] = 1


# list에서 존재 여부 검사하는 것 보다 set에서 존재 여부 검사하는 게 더 빠름