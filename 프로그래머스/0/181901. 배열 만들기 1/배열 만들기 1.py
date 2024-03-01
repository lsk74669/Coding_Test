def solution(n, k):
    limit = n // k
    answer = []
    
    for i in range(1, limit + 1): 
        answer.append(i*k)
    return answer