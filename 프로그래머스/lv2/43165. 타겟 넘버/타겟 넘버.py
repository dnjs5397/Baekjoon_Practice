global result
result = 0

def solution(numbers, target):
    global result
    
    def DFS(idx, c):
        global result
        
        if idx == len(numbers):
            if c == target:
                result += 1
        else:
            DFS(idx+1, c + (-1 * numbers[idx]))
            DFS(idx+1, c + (1 * numbers[idx]))
    
    DFS(0, 0)
    return result