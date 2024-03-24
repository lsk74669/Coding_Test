def solution(my_strings, parts):
    answer = ''
    
    for i, (s, e) in zip(range(0, len(my_strings)), parts):
        for j in range(s, e+1):
            answer += my_strings[i][j]        
    return answer