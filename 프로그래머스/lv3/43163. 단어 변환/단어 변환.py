def solution(begin, target, words):
    if target not in words:
        return 0
    w = dict()
    l = len(begin)


    def DFS(word, cnt):
        for ww in words:
            c = 0
            if ww != word:
                for i in range(l):
                    if ww[i] != word[i]:
                        c += 1
                    if c >= 2:
                        break
                if c < 2:
                    if ww not in w:
                        w[ww] = cnt+1
                        DFS(ww, cnt+1)
                    else:
                        if w[ww] > cnt+1:
                            w[ww] = cnt+1
                            DFS(ww, cnt+1)
                        else:
                            continue


    DFS(begin, 0)
    if target in w:
        return w[target]
    else:
        return 0