n = int(input())

for i in range(0,n):
    left_list = [] # 커서가 중앙에 있다고 가정한 후 좌,우에 스택을 하나씩 둠
    right_list = []
    case = input()
    for j in range(0,len(case)):
        if (case[j] == '-'): # - 문자라면 지워야하니까 왼쪽 스택에서 지워줌
            if (left_list):
                left_list.pop()
        elif (case[j] == '<'): # < 문자라면 커서가 왼쯕으로 하나 옮겨가야하므로 왼쪽 스택에서 뺀 후 오른쪽 스택에 넣어줌
            if (left_list):
                right_list.append(left_list.pop())
        elif (case[j] == '>'): # > 문자라면 커서가 오른쯕으로 하나 옮겨가야하므로 오른쪽 스택에서 뺀 후 왼쪽 스택에 넣어줌
            if (right_list):
                left_list.append(right_list.pop())
        else:
            left_list.append(case[j])  # 그냥 문자라면 left 스택에 넣어줌

    left_list.extend(reversed(right_list)) # 쌓인 순서때문에 (stack이므로) 오른쪽 스택은 뒤집어서 왼쪽 스택과 합쳐준다

    print(''.join(left_list))  # 공백없이 출력