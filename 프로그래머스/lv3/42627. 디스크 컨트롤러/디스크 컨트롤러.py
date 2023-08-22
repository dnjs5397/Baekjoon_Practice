def solution(jobs):
    import heapq
    jobs.sort(key=lambda x: x[0])
    arr = []

    answer = 0
    stime = -1
    etime = 0
    idx = 0
    while (idx < len(jobs)):
        for j in jobs:
            if stime < j[0] <= etime:
                heapq.heappush(arr, [j[1], j[0]])

        if arr:
            t = heapq.heappop(arr)
            stime = etime
            etime += t[0]
            answer += etime - t[1]
            idx += 1
        else:
            etime += 1

    return (answer//len(jobs))