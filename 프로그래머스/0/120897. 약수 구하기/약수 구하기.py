def solution(n):
    LIMIT = int(n**0.5)
    answer = set()
    
    for i in range(1, LIMIT+1):
        if n % i == 0:
            answer.update([i, n//i])
    return list(sorted(answer))