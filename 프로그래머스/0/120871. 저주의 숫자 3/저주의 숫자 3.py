def solution(n):
    answer = 0
    cnt = 0
    
    while n > 0:
        cnt += 1
        if cnt % 3 != 0 and '3' not in str(cnt):
            n -= 1
            answer = cnt
    
    return answer