arr = []
sum = 0.0
c = 0.0
ar = {'A+' : 4.5, 'A0' : 4.0, 'B+' : 3.5, 'B0' : 3.0, 'C+' : 2.5,
      'C0' : 2.0, 'D+' : 1.5, 'D0' : 1.0, 'F' : 0.0}
for _ in range(20):
    s = input()
    a = s.split()
    if a[2] == 'P':
        continue
    c += float(a[1])
    sum += float(a[1]) * float(ar[a[2]])

print(round(sum/c, 6))