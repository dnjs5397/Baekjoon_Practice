def solution(cacheSize, cities):
    # 캐시에 빈 공간이 없다면 바로 return
    if cacheSize == 0:
        return len(cities)*5
    
    answer = 0
    cache = []
    for i in cities:
        i = i.lower() # 대소문자 구별 x
        if len(cache) < cacheSize: #캐시 공간이 남을때
            if i in cache:
                answer += 1
                cache.append(i)
            else:
                cache.append(i)
                answer += 5
        elif len(cache) == cacheSize: # 캐시가 꽉 찼을 때
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