def solution(id_pw, db):
    for info in db:
        if id_pw[0] == info[0]:
            if id_pw[1] == info[1]:
                answer = 'login'
                break
            else:
                answer = 'wrong pw'
                break
        else:
                answer = 'fail'
    return answer
