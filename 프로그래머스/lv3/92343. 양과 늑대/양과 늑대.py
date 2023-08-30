def solution(info, edges):
    answer = []
    visit = [0] * len(info)


    def DFS(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return

        for node in edges:
            if visit[node[0]] == 1 and visit[node[1]] == 0:
                visit[node[1]] = 1
                if info[node[1]] == 0:
                    DFS(sheep+1, wolf)
                else:
                    DFS(sheep, wolf+1)
                visit[node[1]] = 0


    visit[0] = 1
    DFS(1, 0)
    return (max(answer))
