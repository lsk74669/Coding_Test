def solution(n, m, section):
    cnt, i = 0, 0
    
    while i < len(section):
        cnt += 1  
        start = section[i]  
        i += 1

        while i < len(section) and section[i] < start + m:
            i += 1
            
    return cnt
