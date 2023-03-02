def solution(survey, choices):
    
    character = ['R','T','C','F','J','M','A','N']
    cha = dict()
    for c in character:
        cha[c] = 0

    for i in range(len(choices)):
        if choices[i] < 4:
            cha[survey[i][0]] += abs(choices[i]-4)
        else:
            cha[survey[i][1]] += (choices[i]-4)

    answer = ''
    for i in range(0, 8, 2):
        if cha[character[i]] >= cha[character[i+1]]:
            answer += character[i]
        elif cha[character[i]] < cha[character[i+1]]:
            answer += character[i+1]
        else:
            answer += min(character[i+1], character[i])
            
    return answer