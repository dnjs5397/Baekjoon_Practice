N = int(input())
word = []
book = {}
for i in range(N):
    name = input()
    if name not in book:
        book[name] = 1
    else:
        book[name] += 1

maxval = max(book.values())
for i in book.items():
    if i[1] == maxval:
        word.append(i[0])

word.sort()
print(word[0])