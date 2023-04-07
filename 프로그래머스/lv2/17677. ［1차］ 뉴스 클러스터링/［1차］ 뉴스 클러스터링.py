def solution(str1, str2):
    str1, str2 = str1.upper(), str2.upper()
    s1, s2 = [], []
    for i in range(len(str1)-1):
        if (ord(str1[i]) < 65 or ord(str1[i]) > 90) or (ord(str1[i+1]) < 65 or ord(str1[i+1]) > 90):
            continue
        else:
            s1.append(str1[i]+str1[i+1])

    for i in range(len(str2)-1):
        if (ord(str2[i]) < 65 or ord(str2[i]) > 90) or (ord(str2[i+1]) < 65 or ord(str2[i+1]) > 90):
            continue
        else:
            s2.append(str2[i]+str2[i+1])
    if len(s1) == 0 and len(s2) == 0:
        return 65536
    dic = set(s1).union(set(s2))
    set1 = dict()
    set2 = dict()
    for i in s1:
        if i not in set1:
            set1[i] = 1
        else:
            set1[i] += 1
    for i in s2:
        if i not in set2:
            set2[i] = 1
        else:
            set2[i] += 1

    minv = 0
    maxv = 0
    for i in dic:
        if i not in set1:
            maxv += set2[i]
        elif i not in set2:
            maxv += set1[i]
        else:
            minv += min(set1[i], set2[i])
            maxv += max(set1[i], set2[i])

    return (round((minv/maxv)*65536-0.5))