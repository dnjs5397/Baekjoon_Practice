S = input()
zero = 0
one = 0
start = S[0]
for i in S:
    if i != start:
        if start == '0':
            zero += 1
            start = i
        else:
            one += 1
            start = i
            
if S[-1] == '0':
    zero += 1
else:
    one += 1
            
print(min(zero, one))