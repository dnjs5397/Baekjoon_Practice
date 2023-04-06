import sys

for i in range(3):
    case = int(sys.stdin.readline())
    sum = 0
    for j in range(case):
        tmp = int(sys.stdin.readline())
        sum += tmp
    if sum == 0:
        print('0')
    elif sum > 0 :
        print('+')
    else:
        print('-')