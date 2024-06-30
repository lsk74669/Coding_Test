def solution(quiz):
    answer = []
    
    for q in quiz:
        r_q = q.replace('=', '==')
        if bool(eval(r_q)):
            answer.append('O')
        else:
            answer.append('X')
    return answer