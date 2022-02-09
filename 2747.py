def fibo(data):
    fi = []
    fi.append(0)
    fi.append(1)
    if (data >= 2):
        for i in range(2, data+1):
            fi.append(fi[i-2] + fi[i-1])
    return fi[data]
        
    
a = int(input())
print(fibo(a)%1234567)

# 다른 풀이
# n = int(input())

# a, b = 0, 1

# while n > 0:
#     a, b = b, a+b
#     n -= 1
# print(a)