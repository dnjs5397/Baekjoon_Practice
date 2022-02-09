N = int(input())
max = 0
book = []
answer = []
for i in range(N):
    book.append(input())

for i in book:
    if book.count(i) > max:
        max = book.count(i)
        
for i in book:
    if book.count(i) == max:
        if i not in answer:
            answer.append(i)
        else:
            pass

answer.sort()
print(answer[0])