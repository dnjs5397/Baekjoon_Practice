def GCD(x,y):
    while(y):
        x,y = y, x%y
    return x

def LCM(x,y):
    result = (x*y)//GCD(x,y)
    return result

count = 0
N = int(input())
if N <= 10:
    print(0)
    exit(0)
hate = []
length = len(str(N))
tmp = '1'
for i in range(2, length+1):
    tmp += '1'
    hate.append(int(tmp))
if N < int(tmp):
    hate.pop()

tmp_hate = []

for i in range(len(hate)-1):
    for j in range(i+1, len(hate)):
        if hate[j] % hate[i] == 0:
            if hate[j] not in tmp_hate:
                tmp_hate.append(hate[j])


for i in tmp_hate:
    hate.remove(i)

print(hate)

is_in  = False
for i in hate:
    count += N // i
    if N % i == 0:
        count -= 1
        if is_in == False:
            count += 1
            is_in = True

lcm = []
real_lcm = []
for i in range(len(hate)-1):
    for j in range(i+1, len(hate)):
        real_lcm.append(LCM(hate[i], hate[j]))
        
for i in range(len(lcm)-1):
    for j in range(i+1, len(lcm)):
        if lcm[j] % lcm[i] == 0:
            if lcm[j] not in real_lcm:
                real_lcm.append(lcm[j])

for i in real_lcm:
    count += (N // i)
        
print(count)