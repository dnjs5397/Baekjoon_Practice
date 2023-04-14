def solution(n, times):
    left = 1
    right = max(times) * n
    result = []
    while (left <= right):
        person = 0
        mid = (left + right) // 2
        for i in times:
            person += (mid // i)
        if person >= n:
            result.append(mid)
            right = mid - 1
        else:
            left = mid + 1

    return min(result)