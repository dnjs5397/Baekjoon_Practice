# 크로아티아 알파벳
count = 0
s = input()
length = len(s)
cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in cro:
    if s.find(i) != -1:
        count += s.count(i)
        s = s.replace(i, ' ')

for i in s:
    if i != ' ' and i != '=' and i != '-':
        count += 1

print(count)