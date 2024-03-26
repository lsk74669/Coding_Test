def solution(s):
    answer = []
    for idx_1,i in enumerate(s):
        if idx_1 == 0:
            answer.append(-1)
        else:
            temp = []
            
            for idx_2, j in enumerate(s[:idx_1]):
                if i == j:
                    temp.append(idx_1 - idx_2)
                    
            if len(temp) >= 1:
                answer.append(min(temp))
            else:
                answer.append(-1)
        
    return answer