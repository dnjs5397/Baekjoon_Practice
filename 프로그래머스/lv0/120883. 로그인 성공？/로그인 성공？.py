def solution(id_pw, db):
    id = False
    pw = False
    for i in db:
        if i[0] == id_pw[0] and i[1] == id_pw[1]:
            return 'login'
        elif id_pw[0] == i[0]:
            id = True
    
    if id == False and pw == False:
        return 'fail'
    else:
        return 'wrong pw'