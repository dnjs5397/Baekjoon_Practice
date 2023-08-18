def solution(n, k):
    def check(number):
        for i in range(2, int(number**0.5)+1):
            if number % i == 0:
                return False
        return True
    num = []
    if k != 10:
        while (n >= k):
            num.insert(0, str(n % k))
            n = n // k
        num.insert(0, str(n))
        st = ''.join(num)
    else:
        st = str(n)
    index = []

    for i in range(len(st)):
        if st[i] == '0':
            index.append(i)
            
    if index == []:
        if check(int(st)):
            return 1
        
    real = []
    for i in range(len(index)):
        if i == 0:
            real.append(st[:index[i]])
        elif i == len(index)-1:
            real.append(st[index[i-1]+1:index[i]])
            real.append(st[index[i]+1:])
        else:
            real.append(st[index[i-1]+1:index[i]])




    global answer
    answer = 0
    for i in real:
        if i == '1' or i == '':
            continue
        else:
            if check(int(i)):
                answer += 1

    return answer