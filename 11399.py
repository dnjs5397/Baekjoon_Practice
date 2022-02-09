while(1):
    try:
        jump = list(map(int, input().split()))
        print(max(jump[2]-jump[1]-1, jump[1]-jump[0]-1))
    except:
        break