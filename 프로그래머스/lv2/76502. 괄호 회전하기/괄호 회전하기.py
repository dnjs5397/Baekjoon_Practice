def check(arr):
    stack = []
    
    for i in arr:
        if stack and stack[-1] == '[' and i == ']':
            del stack[-1]
        elif stack and stack[-1] == '(' and i == ')':
            del stack[-1]
        elif stack and stack[-1] == '{' and i == '}':
            del stack[-1]
        else:
            stack.append(i)
    
    if stack == []:
        return True
    else:
        return False

def solution(s):
    cnt = 0
    for i in range(len(s)):
        tmp = s[0]
        s = s[1:] + tmp
        if check(s):
            cnt += 1

    return cnt