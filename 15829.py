L = int(input())
s = input()
result = 0
for i in range(L):
    num = ord(s[i]) - 96
    result += num * pow(31, i)
print(result % 1234567891)