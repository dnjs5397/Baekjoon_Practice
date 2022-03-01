# 그룹 단어 체커
N = int(input())
count = 0
for _ in range(N):
    is_true = True
    word = input()
    for i in word:
        tmp = ''
        for j in range(word.count(i)):
            tmp += i
        if tmp in word:
            pass
        else:
            is_true = False
    if is_true:
        count += 1

print(count)
            
            