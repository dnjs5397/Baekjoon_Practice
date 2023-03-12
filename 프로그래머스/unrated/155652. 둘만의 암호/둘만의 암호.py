def solution(s, skip, index):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    alp = []
    result = ''
    for i in alpha:
        if i not in skip:
            alp.append(i)
    
    maxindex = len(alp)
    
    for i in s:
        idx = alp.index(i)
        idx += index
        idx = idx % maxindex
        result += alp[idx]

    return result