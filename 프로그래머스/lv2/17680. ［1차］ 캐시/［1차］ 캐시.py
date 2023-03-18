def solution(cacheSize, cities):
    
    if cacheSize == 0:
        return len(cities)*5
    
    answer = 0
    cache = []
    for i in cities:
        i = i.lower()
        if len(cache) < cacheSize:
            if i in cache:
                answer += 1
                cache.append(i)
            else:
                cache.append(i)
                answer += 5
        elif len(cache) == cacheSize:
            if i in cache:
                answer += 1
                idx = cache.index(i)
                cache.pop(idx)
                cache.append(i)
            else:
                cache.pop(0)
                cache.append(i)
                answer += 5
                
    return answer