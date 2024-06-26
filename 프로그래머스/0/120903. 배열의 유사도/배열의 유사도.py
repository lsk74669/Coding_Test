def solution(s1, s2):
    answer = 0
    
    for str in s2:
        if str in s1:
            answer += 1
    return answer