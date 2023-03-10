def solution(X, Y):
    xanswer = dict()
    yanswer = dict()
    result = []
    xlist = list(set(X))
    for i in X:
        xanswer[i] = 0
        yanswer[i] = 0    
    for i in Y:
        yanswer[i] = 0    
        xanswer[i] = 0

    for i in X:
        xanswer[i] += 1 
    for i in Y:
        yanswer[i] += 1 

    for i in xlist:
        if xanswer.get(i) != 0 and yanswer.get(i) != 0:
            tmp = [int(i)] * min(xanswer.get(i), yanswer.get(i))
            result.append(tmp)


    result = [item for sublist in result for item in sublist]
    result.sort(reverse=True)

    if result == []:
        return '-1'
    if set(result) == {0}:
        return '0'
    else:
        dap = ''
        for i in result:
            dap += str(i)
        return dap