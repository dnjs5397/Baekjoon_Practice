S = input()
length = len(S)
count0 = 0
count1 = 0
if S[0] == '0':
    count1 += 1
else:
    count0 += 1
    
for i in range(length-1):
    if S[i] != S[i+1]:
        if S[i+1] == '0':
            count1 += 1
        else:
            count0 += 1
print(min(count0, count1))