def solution(num_list):
    total_cnt = 0
    
    for i in num_list:
        cnt = 0
        
        while i != 1:
            cnt += 1
            if i % 2 == 0:
                i /= 2
            else:
                i = (i-1)/2
                
        total_cnt += cnt
            
    return total_cnt