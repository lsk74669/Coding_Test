def solution(i, j, k):
    k = str(k)
    
    cnt = 0
    for num in range(i, j + 1):
        cnt += str(num).count(k)
    
    return cnt
