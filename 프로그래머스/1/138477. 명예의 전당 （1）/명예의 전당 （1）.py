def solution(k, score):
    temp = []
    answer = []
    
    for i in score:
        temp.append(i)
        if len(temp) > k:
            temp.remove(min(temp))
        answer.append(min(temp))
        
            
    return answer