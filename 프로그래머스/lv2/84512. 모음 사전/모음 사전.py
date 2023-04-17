def solution(word):
    words = 'AEIOU'
    result = []
    def DFS(v, w):
        if v == 5:
            return
        for i in range(len(words)):
            result.append(w + words[i])
            DFS(v+1, w + words[i])

    DFS(0, '')
    return (result.index(word)+1)