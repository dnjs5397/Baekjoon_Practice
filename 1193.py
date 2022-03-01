# 분수 찾기
X = int(input())
number = []
num = 0
i = 1
while(num <= X):
    num += i
    i += 1
    number.append(num)
index = 0
a = 0
b = 0
for i in range(len(number)):
    if X <= number[i]:
        b = number[i] - X + 1
        a = i+2 - b
        if (i+1) % 2 == 0:
            print(a, '/', b, sep='')
        else:
            print(b, '/', a, sep='')
        break


