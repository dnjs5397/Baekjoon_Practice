def solution(s, k):
    num = 0
    idx = 0
    arr = []
    for i in range(len(s)):
        num += s[i]
        if num == k:
            arr.append([i-idx, idx, i])

        while (num > k):
            num -= s[idx]
            idx += 1
            if num == k:
                arr.append([i-idx, idx, i])

    arr.sort(key=lambda x: x[1])
    arr.sort(key=lambda x: x[0])
    return ([arr[0][1], arr[0][2]])
