def solution(babbling):
    arr = ["aya", "ye", "woo", "ma" ]
    result = 0
    for i in babbling:
        tmp = i
        for j in range(len(arr)):
            if arr[j]*2 not in tmp:
                tmp = tmp.replace(arr[j], ' ')

        if set(tmp) == {' '}:
            result += 1

    return result
