def solution(strArr):
    answer = []
    for idx, s in enumerate(strArr):
        if idx % 2 == 0:
            answer.append(s.lower())
        else:
            answer.append(s.upper())
            
    return answer