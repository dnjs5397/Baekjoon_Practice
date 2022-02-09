# N = int(input()) # 스테이지 개수
# stages = [4,4,4,4] # 멈춰있는 스테이지 번호

# def solution(N, stages):
#     player = len(stages)
#     stay = list(0 for i in range(N+2))
#     answer = []

#     for i in range(player):
#         stay[stages[i]] += 1
    
#     for i in range(1,N+1):
#         if (stay[i] == 0):
#             answer.append(0.0)
#         else:
#             answer.append(stay[i] / player)
#             player -= stay[i]

#     answer = sorted(range(len(answer)), key=answer.__getitem__, reverse=True)
#     for i in range(len(answer)):
#         answer[i] += 1

#     return answer


result = 0
c_value = 0
l_value = []
a_count = 0
dartResult = "1S*2T*3S"
dartResult += " "
length = len(dartResult)
for i in range(length):
    if (a_count == 3):
        result = l_value[0] + l_value[1] + l_value[2]
        break
    temp = ""
    if (ord(dartResult[i]) >= 48 and ord(dartResult[i]) <= 57):
        temp += dartResult[i]
        if (dartResult[i] == "1"):
            if (dartResult[i+1] == "0"):
                temp += "0"
                i += 1
        c_value += int(temp)
        l_value.append(c_value)
    elif (dartResult[i] == "S"):
        a_count += 1
        if (dartResult[i+1] == "*"):
            if (a_count == 3):
                l_value[2] *= 2
                l_value[1] *= 2
                i += 1
                c_value = 0
            elif (a_count == 2):
                l_value[1] *= 2
                l_value[0] *= 2
                i += 1
                c_value = 0
            else:
                l_value[0] *= 2
                c_value = 0
        elif (dartResult[i+1] == "#"):
            l_value[a_count-1] *= -1
            i += 1
            c_value = 0
        else:
            c_value = 0
            
    elif (dartResult[i] == "D"):
        a_count += 1
        l_value[a_count-1] = c_value*c_value
        
        if (dartResult[i+1] == "*"):
            if (a_count == 3):
                l_value[2] *= 2
                l_value[1] *= 2
                i += 1
                c_value = 0
            elif (a_count == 2):
                l_value[1] *= 2
                l_value[0] *= 2
                i += 1
                c_value = 0
            else:
                l_value[0] *= 2
                c_value = 0
        elif (dartResult[i+1] == "#"):
            l_value[a_count-1] *= -1
            i += 1
            c_value = 0
        else:
            c_value = 0
            
            
        
    elif (dartResult[i] == "T"):
        a_count += 1
        l_value[a_count-1] = c_value*c_value*c_value
        if (dartResult[i+1] == "*"):
            if (a_count == 3):
                l_value[2] *= 2
                l_value[1] *= 2
                i += 1
                c_value = 0
            elif (a_count == 2):
                l_value[1] *= 2
                l_value[0] *= 2
                i += 1
                c_value = 0
            else:
                l_value[0] *= 2
                c_value = 0
        elif (dartResult[i+1] == "#"):
            l_value[a_count-1] *= -1
            i += 1
            c_value = 0
        else:
            c_value = 0
print(result)