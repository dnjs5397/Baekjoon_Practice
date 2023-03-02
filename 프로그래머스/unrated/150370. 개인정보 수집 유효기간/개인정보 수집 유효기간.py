def solution(today, terms, privacies):
    policy = {}
    result = []

    t_years = int(today[:4])
    t_months = int(today[5:7])
    t_days = int(today[8:10])

    for term in terms :
        policy[term[0]] = term[2:]

    index = 0
    for index in range(len(privacies)):
        years = int(privacies[index][:4])
        months = int(privacies[index][5:7])
        days = int(privacies[index][8:10])
        priv = privacies[index][-1]
        months += int(policy[priv])
        days -= 1
        if days == 0:
            days = 28
            months -= 1
            if months == 0:
                months = 12
                years -= 1

        if months > 12:
            years += (months//12)
            months = (months%12)
            if months == 0:
                months = 12
                years -= 1

        if days < 1:
            days = 28
            months -= 1
            if months < 1:
                months = 12
                years -= 1

        print(years, months, days)
        print(t_years, t_months, t_days)
        if years < t_years:
            result.append(index+1)
        elif (years == t_years and months < t_months):
            result.append(index+1)
        elif (years == t_years and months == t_months):
            if days < t_days:
                result.append(index+1)
                
                
    return sorted(result)