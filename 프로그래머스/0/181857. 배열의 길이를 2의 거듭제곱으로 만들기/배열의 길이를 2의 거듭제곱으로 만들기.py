def solution(arr):
    answer = arr.copy()
    n = len(arr)
    i = 0
    
    while n > 2 ** i:
        i += 1
    
    m = (2 ** i) - n
    
    for _ in range(m):
        answer.append(0)
    
    return answer