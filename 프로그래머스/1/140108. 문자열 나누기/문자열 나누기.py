def solution(s):
    cnt = 0
    i = 0
    
    while i < len(s):
        x = s[i]
        cnt_x = 0
        cnt_not_x = 0
        
        while i < len(s):
            if s[i] == x:
                cnt_x += 1
            else:
                cnt_not_x += 1
            i += 1
            
            if cnt_x == cnt_not_x:
                break
        
        cnt += 1
    
    return cnt
